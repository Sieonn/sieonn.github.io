# 프레임 접기/펼치기 모션 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** `SplitView.tsx`에서 프레임 하나가 접히거나 펼쳐질 때(한쪽 패널만 접힘/펼침 전환) 크기 변화와 셰브론 회전에 420ms 애니메이션을 적용한다.

**Architecture:** `react-reflex`의 `ReflexElement`는 실제로 `React.forwardRef`로 DOM `<div>`에 `ref`를 그대로 전달한다(`.d.ts`는 일반 class로 잘못 선언돼 있어 캐스팅 필요). `SplitView.tsx`(클래스 컴포넌트)의 `getSnapshotBeforeUpdate`/`componentDidUpdate` 생명주기로 전환 전/후 픽셀 크기를 측정하고, 순수 유틸 `SplitView.motion.ts`의 `animatePaneResize()`가 `flexGrow`/`flexShrink`/`minWidth`/`minHeight`를 잠근 뒤 `Element.animate()`(Web Animations API)로 width 또는 height를 보간한다. 전환 감지는 `SplitView.layout.ts`의 새 순수 함수 `classifySplitLayoutMode()` + `getTransitioningPane()`이 담당하며, "한쪽만 접힘/펼침" 케이스만 애니메이션 대상으로 분류한다(양쪽 동시 접힘·expand·strip·merged bar는 `'other'`로 분류되어 기존처럼 즉시 스냅).

**Tech Stack:** React 17 + TypeScript, MobX(`inject`/`observer`), `react-reflex`, Web Animations API(`Element.animate`), Vitest(jsdom).

## Global Constraints

- 모션 값은 스펙 그대로 고정: 크기/셰브론 전환 duration `420ms`, easing `cubic-bezier(.32,.9,.24,1)`. 다른 값을 새로 만들지 않는다.
- 목표/시작 크기 차이가 `1.5px` 미만이면 애니메이션을 생략한다.
- `prefers-reduced-motion: reduce`이면 애니메이션 없이 즉시 최종 상태로 전환한다.
- 애니메이션 도중 재전환(재클릭)이 발생하면 처음 크기로 되돌아가지 않고 현재 렌더 크기에서 이어받는다.
- 드래그 리사이즈(`onStopResize`)에는 이 모션이 절대 개입하지 않는다 — 트리거는 오직 접힘 상태 전환뿐이다.
- 이번 변경 범위 밖(양쪽 동시 접힘, expand, merged bar, strip 모드, 본문 페이드인)은 기존 동작(즉시 스냅)을 그대로 유지하며 회귀시키지 않는다.
- 설계 근거: `docs/superpowers/specs/2026-07-31-frame-collapse-motion-design.md`

---

### Task 1: Vitest에 SplitView 테스트 포함시키기

**배경:** `src/components/SplitView.layout.test.ts`가 이미 존재하지만 `vitest.config.ts`의 `test.include`가
`src/ai-builder`, `src/components/aiAutomation`, `src/components/automation`, `src/components/store` 4개
폴더만 화이트리스트로 잡고 있어 이 테스트는 현재 `npm run test:run`으로 실행되지 않는다
(`npx vitest run src/components/SplitView.layout.test.ts` → `No test files found`으로 직접 확인함).
이번 작업에서 추가할 `SplitView.motion.test.ts`도 마찬가지로 실행되지 않을 것이므로 먼저 include를 넓힌다.

**Files:**
- Modify: `vitest.config.ts:17-22`

**Interfaces:**
- 이 태스크는 설정 변경만 하며 코드 인터페이스를 만들지 않는다.

- [ ] **Step 1: include 목록에 SplitView 테스트 패턴 추가**

`vitest.config.ts`의 `include` 배열을 아래와 같이 수정한다.

```ts
include: [
  'src/ai-builder/**/*.test.{ts,tsx}',
  'src/components/aiAutomation/**/*.test.{ts,tsx}',
  'src/components/automation/**/*.test.{ts,tsx}',
  'src/components/store/**/*.test.{ts,tsx}',
  'src/components/SplitView*.test.{ts,tsx}',
],
```

- [ ] **Step 2: 기존 SplitView.layout.test.ts가 실행되는지 확인**

Run: `npx vitest run src/components/SplitView.layout.test.ts`
Expected: 기존 테스트 케이스들이 전부 PASS (이 파일의 테스트 내용은 건드리지 않았으므로 실행만 되면 됨).

- [ ] **Step 3: Commit**

```bash
git add vitest.config.ts
git commit -m "test: SplitView 테스트 파일이 vitest에서 실행되도록 include 추가"
```

---

### Task 2: 레이아웃 전환 분류기 (`classifySplitLayoutMode`, `getTransitioningPane`)

**Files:**
- Modify: `src/components/SplitView.layout.ts` (파일 끝에 추가)
- Test: `src/components/SplitView.layout.test.ts` (파일 끝에 추가)

**Interfaces:**
- Produces:
  - `export type SplitLayoutMode = 'normal' | 'first-collapsed' | 'second-collapsed' | 'other'`
  - `export interface SplitLayoutModeInput { firstExpanded: boolean; secondExpanded: boolean; shouldUseEqualWidthCollapsedRow: boolean; firstStripAffectsSplitLayout: boolean; secondStripAffectsSplitLayout: boolean; firstContentCollapsed: boolean; secondContentCollapsed: boolean; }`
  - `export function classifySplitLayoutMode(input: SplitLayoutModeInput): SplitLayoutMode`
  - `export function getTransitioningPane(prev: SplitLayoutMode | null, next: SplitLayoutMode): 'first' | 'second' | null`

- [ ] **Step 1: 실패하는 테스트 작성**

`src/components/SplitView.layout.test.ts` 파일 끝에 추가:

```ts
import { classifySplitLayoutMode, getTransitioningPane } from './SplitView.layout'

describe('classifySplitLayoutMode', () => {
  const BASE_MODE_INPUT = {
    firstExpanded: false,
    secondExpanded: false,
    shouldUseEqualWidthCollapsedRow: false,
    firstStripAffectsSplitLayout: false,
    secondStripAffectsSplitLayout: false,
    firstContentCollapsed: false,
    secondContentCollapsed: false,
  }

  it('둘 다 펼쳐져 있으면 normal', () => {
    expect(classifySplitLayoutMode(BASE_MODE_INPUT)).toBe('normal')
  })

  it('첫 번째만 접히면 first-collapsed', () => {
    expect(classifySplitLayoutMode({ ...BASE_MODE_INPUT, firstContentCollapsed: true })).toBe('first-collapsed')
  })

  it('두 번째만 접히면 second-collapsed', () => {
    expect(classifySplitLayoutMode({ ...BASE_MODE_INPUT, secondContentCollapsed: true })).toBe('second-collapsed')
  })

  it('양쪽 다 접히면 other (v1 애니메이션 대상 아님)', () => {
    expect(classifySplitLayoutMode({ ...BASE_MODE_INPUT, firstContentCollapsed: true, secondContentCollapsed: true })).toBe('other')
  })

  it('firstExpanded면 other', () => {
    expect(classifySplitLayoutMode({ ...BASE_MODE_INPUT, firstExpanded: true })).toBe('other')
  })

  it('equal-width collapsed row면 other', () => {
    expect(classifySplitLayoutMode({ ...BASE_MODE_INPUT, shouldUseEqualWidthCollapsedRow: true })).toBe('other')
  })

  it('strip이 레이아웃에 영향을 주면 other', () => {
    expect(classifySplitLayoutMode({ ...BASE_MODE_INPUT, firstStripAffectsSplitLayout: true })).toBe('other')
  })
})

describe('getTransitioningPane', () => {
  it('normal -> first-collapsed면 first', () => {
    expect(getTransitioningPane('normal', 'first-collapsed')).toBe('first')
  })

  it('first-collapsed -> normal이면 first', () => {
    expect(getTransitioningPane('first-collapsed', 'normal')).toBe('first')
  })

  it('normal -> second-collapsed면 second', () => {
    expect(getTransitioningPane('normal', 'second-collapsed')).toBe('second')
  })

  it('second-collapsed -> normal이면 second', () => {
    expect(getTransitioningPane('second-collapsed', 'normal')).toBe('second')
  })

  it('모드가 같으면 null', () => {
    expect(getTransitioningPane('normal', 'normal')).toBe(null)
  })

  it('other가 관여하면 null', () => {
    expect(getTransitioningPane('other', 'first-collapsed')).toBe(null)
    expect(getTransitioningPane('first-collapsed', 'other')).toBe(null)
  })

  it('first-collapsed -> second-collapsed 직행은 null (v1 미지원)', () => {
    expect(getTransitioningPane('first-collapsed', 'second-collapsed')).toBe(null)
  })

  it('prev가 null이면 null (최초 렌더)', () => {
    expect(getTransitioningPane(null, 'normal')).toBe(null)
  })
})
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `npx vitest run src/components/SplitView.layout.test.ts`
Expected: FAIL — `classifySplitLayoutMode`/`getTransitioningPane`가 존재하지 않음 (import error).

- [ ] **Step 3: 구현 작성**

`src/components/SplitView.layout.ts` 파일 끝에 추가:

```ts
export type SplitLayoutMode = 'normal' | 'first-collapsed' | 'second-collapsed' | 'other';

export interface SplitLayoutModeInput {
  firstExpanded: boolean;
  secondExpanded: boolean;
  shouldUseEqualWidthCollapsedRow: boolean;
  firstStripAffectsSplitLayout: boolean;
  secondStripAffectsSplitLayout: boolean;
  firstContentCollapsed: boolean;
  secondContentCollapsed: boolean;
}

/** 이 pane 쌍의 이번 렌더가 "한쪽만 접힘/펼침" 애니메이션 대상인지 분류한다. */
export function classifySplitLayoutMode(input: SplitLayoutModeInput): SplitLayoutMode {
  const {
    firstExpanded,
    secondExpanded,
    shouldUseEqualWidthCollapsedRow,
    firstStripAffectsSplitLayout,
    secondStripAffectsSplitLayout,
    firstContentCollapsed,
    secondContentCollapsed,
  } = input;

  if (
    firstExpanded ||
    secondExpanded ||
    shouldUseEqualWidthCollapsedRow ||
    firstStripAffectsSplitLayout ||
    secondStripAffectsSplitLayout
  ) {
    return 'other';
  }
  if (firstContentCollapsed && secondContentCollapsed) {
    return 'other';
  }
  if (firstContentCollapsed) {
    return 'first-collapsed';
  }
  if (secondContentCollapsed) {
    return 'second-collapsed';
  }
  return 'normal';
}

/** 직전/이번 레이아웃 모드로부터 크기 애니메이션을 태울 pane을 판정한다. v1은 normal <-> 단일 collapsed 전환만 지원한다. */
export function getTransitioningPane(
  prev: SplitLayoutMode | null,
  next: SplitLayoutMode,
): 'first' | 'second' | null {
  if (prev == null || prev === next) {
    return null;
  }
  if (
    (prev === 'normal' && next === 'first-collapsed') ||
    (prev === 'first-collapsed' && next === 'normal')
  ) {
    return 'first';
  }
  if (
    (prev === 'normal' && next === 'second-collapsed') ||
    (prev === 'second-collapsed' && next === 'normal')
  ) {
    return 'second';
  }
  return null;
}
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `npx vitest run src/components/SplitView.layout.test.ts`
Expected: PASS (기존 케이스 포함 전체)

- [ ] **Step 5: Commit**

```bash
git add src/components/SplitView.layout.ts src/components/SplitView.layout.test.ts
git commit -m "feat: SplitView 레이아웃 전환 분류 유틸(classifySplitLayoutMode, getTransitioningPane) 추가"
```

---

### Task 3: 패널 크기 보간 유틸 (`SplitView.motion.ts`)

**Files:**
- Create: `src/components/SplitView.motion.ts`
- Create: `src/components/SplitView.motion.test.ts`

**Interfaces:**
- Consumes: 없음 (독립 유틸)
- Produces:
  - `export const FOLD_DURATION_MS = 420`
  - `export const FOLD_EASING = 'cubic-bezier(.32,.9,.24,1)'`
  - `export function getPrefersReducedMotion(): boolean`
  - `export function animatePaneResize(el: HTMLElement, from: number, to: number, axis: 'width' | 'height', prefersReducedMotion: boolean): void`

- [ ] **Step 1: 실패하는 테스트 작성**

`src/components/SplitView.motion.test.ts`:

```ts
import { animatePaneResize, FOLD_DURATION_MS, FOLD_EASING } from './SplitView.motion'

function createMockAnimation() {
  const listeners: Record<string, () => void> = {};
  return {
    cancel: vi.fn(),
    addEventListener: (event: string, cb: () => void) => {
      listeners[event] = cb;
    },
    fireFinish: () => listeners['finish']?.(),
  };
}

function createMockEl(rect: { width: number; height: number }) {
  const animation = createMockAnimation();
  const el = {
    style: {} as Record<string, string>,
    getBoundingClientRect: vi.fn().mockReturnValue(rect),
    animate: vi.fn().mockReturnValue(animation),
  };
  return { el, animation };
}

describe('animatePaneResize', () => {
  it('prefersReducedMotion이면 animate를 호출하지 않는다', () => {
    const { el } = createMockEl({ width: 40, height: 100 });
    animatePaneResize(el as unknown as HTMLElement, 40, 400, 'width', true);
    expect(el.animate).not.toHaveBeenCalled();
  });

  it('from/to 차이가 1.5px 미만이면 animate를 호출하지 않는다', () => {
    const { el } = createMockEl({ width: 40, height: 100 });
    animatePaneResize(el as unknown as HTMLElement, 40, 41, 'width', false);
    expect(el.animate).not.toHaveBeenCalled();
  });

  it('정상 전환이면 스펙 값(420ms, cubic-bezier)으로 width를 보간한다', () => {
    const { el } = createMockEl({ width: 40, height: 100 });
    animatePaneResize(el as unknown as HTMLElement, 40, 400, 'width', false);

    expect(el.animate).toHaveBeenCalledWith(
      [{ width: '40px' }, { width: '400px' }],
      expect.objectContaining({ duration: FOLD_DURATION_MS, easing: FOLD_EASING, fill: 'both' }),
    );
  });

  it('애니메이션 도중 flexGrow/flexShrink/minWidth를 잠그고, 완료 후 원복한다', () => {
    const { el, animation } = createMockEl({ width: 40, height: 100 });
    el.style.flexGrow = '1';
    el.style.flexShrink = '1';
    el.style.minWidth = '150px';

    animatePaneResize(el as unknown as HTMLElement, 40, 400, 'width', false);
    expect(el.style.flexGrow).toBe('0');
    expect(el.style.flexShrink).toBe('0');
    expect(el.style.minWidth).toBe('0');

    animation.fireFinish();
    expect(el.style.flexGrow).toBe('1');
    expect(el.style.flexShrink).toBe('1');
    expect(el.style.minWidth).toBe('150px');
  });

  it('진행 중인 애니메이션이 있으면 취소하고 현재 렌더 크기에서 이어받는다', () => {
    const { el, animation } = createMockEl({ width: 40, height: 100 });

    animatePaneResize(el as unknown as HTMLElement, 40, 400, 'width', false);
    (el.getBoundingClientRect as any).mockReturnValue({ width: 220, height: 100 });

    animatePaneResize(el as unknown as HTMLElement, 400, 40, 'width', false);

    expect(animation.cancel).toHaveBeenCalledTimes(1);
    expect(el.animate).toHaveBeenLastCalledWith(
      [{ width: '220px' }, { width: '40px' }],
      expect.objectContaining({ duration: FOLD_DURATION_MS, easing: FOLD_EASING }),
    );
  });
});
```

- [ ] **Step 2: 테스트 실패 확인**

Run: `npx vitest run src/components/SplitView.motion.test.ts`
Expected: FAIL — 모듈 `./SplitView.motion`이 존재하지 않음.

- [ ] **Step 3: 구현 작성**

`src/components/SplitView.motion.ts`:

```ts
export const FOLD_DURATION_MS = 420;
export const FOLD_EASING = 'cubic-bezier(.32,.9,.24,1)';
const MIN_ANIMATABLE_DELTA_PX = 1.5;

const runningAnimations = new WeakMap<HTMLElement, Animation>();

export function getPrefersReducedMotion(): boolean {
  if (typeof window === 'undefined' || typeof window.matchMedia !== 'function') {
    return false;
  }
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}

/**
 * 패널 접힘/펼침 전환 시 width 또는 height를 스펙값(420ms, cubic-bezier(.32,.9,.24,1))으로 보간한다.
 * 진행 중인 애니메이션이 있으면 현재 렌더 크기를 새 시작점으로 이어받는다(처음 위치로 스냅되지 않음).
 */
export function animatePaneResize(
  el: HTMLElement,
  from: number,
  to: number,
  axis: 'width' | 'height',
  prefersReducedMotion: boolean,
): void {
  const running = runningAnimations.get(el);
  let actualFrom = from;
  if (running != null) {
    const rect = el.getBoundingClientRect();
    actualFrom = axis === 'width' ? rect.width : rect.height;
    running.cancel();
    runningAnimations.delete(el);
  }

  if (prefersReducedMotion || Math.abs(actualFrom - to) < MIN_ANIMATABLE_DELTA_PX) {
    return;
  }

  const prevFlexGrow = el.style.flexGrow;
  const prevFlexShrink = el.style.flexShrink;
  const prevMinWidth = el.style.minWidth;
  const prevMinHeight = el.style.minHeight;

  const restore = () => {
    el.style.flexGrow = prevFlexGrow;
    el.style.flexShrink = prevFlexShrink;
    el.style.minWidth = prevMinWidth;
    el.style.minHeight = prevMinHeight;
  };

  el.style.flexGrow = '0';
  el.style.flexShrink = '0';
  if (axis === 'width') {
    el.style.minWidth = '0';
  }
  else {
    el.style.minHeight = '0';
  }

  const animation = el.animate(
    [{ [axis]: `${actualFrom}px` }, { [axis]: `${to}px` }],
    { duration: FOLD_DURATION_MS, easing: FOLD_EASING, fill: 'both' },
  );
  runningAnimations.set(el, animation);

  animation.addEventListener('finish', () => {
    runningAnimations.delete(el);
    restore();
  });
}
```

- [ ] **Step 4: 테스트 통과 확인**

Run: `npx vitest run src/components/SplitView.motion.test.ts`
Expected: PASS (5개 케이스 전부)

- [ ] **Step 5: Commit**

```bash
git add src/components/SplitView.motion.ts src/components/SplitView.motion.test.ts
git commit -m "feat: 패널 접힘/펼침 크기 보간 유틸(animatePaneResize) 추가"
```

---

### Task 4: `SplitView.tsx`에 크기 보간 배선

**Files:**
- Modify: `src/components/SplitView.tsx`

**Interfaces:**
- Consumes:
  - `classifySplitLayoutMode`, `getTransitioningPane`, `SplitLayoutMode` from `./SplitView.layout` (Task 2)
  - `animatePaneResize`, `getPrefersReducedMotion` from `./SplitView.motion` (Task 3)
- Produces: 없음 (컴포넌트 내부 배선, 다른 태스크가 참조하지 않음)

**주의:** `react-reflex`의 `ReflexElement` default export는 런타임에는 `React.forwardRef`로 실제
DOM `<div>`에 ref를 전달하지만(`node_modules/react-reflex/dist/commonjs/ReflexElement.js` 확인),
패키지의 `index.d.ts`는 이를 일반 class(`class ReflexElement extends React.Component<...>`)로만
선언해 놓아 TypeScript가 `ref`를 `HTMLDivElement`가 아닌 컴포넌트 인스턴스로 추론한다. 아래처럼
`as unknown as React.Ref<InstanceType<typeof ReflexElement>>`로 캐스팅한다.

- [ ] **Step 1: import 추가**

`src/components/SplitView.tsx` 상단 import 블록(1~24행)에 추가:

```ts
import {
  resolveSplitLayout,
  shouldRenderMergedBar,
  shouldShowCollapsedBarTitle,
  classifySplitLayoutMode,
  getTransitioningPane,
  SplitLayoutMode,
} from './SplitView.layout';
import { animatePaneResize, getPrefersReducedMotion } from './SplitView.motion';
```

(기존 `import { resolveSplitLayout, shouldRenderMergedBar, shouldShowCollapsedBarTitle } from './SplitView.layout';` 줄을 위 블록으로 교체한다.)

- [ ] **Step 2: 인스턴스 필드 추가**

클래스 필드 선언부(`private hideTooltipTimer` 근처, 159행 위)에 추가:

```ts
private firstPaneRef = React.createRef<HTMLDivElement>();
private secondPaneRef = React.createRef<HTMLDivElement>();
private prevLayoutMode: SplitLayoutMode | null = null;
private currentLayoutMode: SplitLayoutMode = 'other';
private currentAxis: 'width' | 'height' = 'width';
```

- [ ] **Step 3: render()에서 레이아웃 모드 계산 및 저장**

`render()`의 merged-bar 조기 return 직전(408행 `if (shouldRenderMergedBar({`) 바로 위에 추가:

```ts
this.currentLayoutMode = 'other';
this.currentAxis = isVerticalStackSplit ? 'height' : 'width';
```

그리고 `resolveSplitLayout` 호출 직후(464행, `} = resolveSplitLayout({...});` 다음 줄)에 추가:

```ts
this.currentLayoutMode = classifySplitLayoutMode({
  firstExpanded,
  secondExpanded,
  shouldUseEqualWidthCollapsedRow,
  firstStripAffectsSplitLayout,
  secondStripAffectsSplitLayout,
  firstContentCollapsed,
  secondContentCollapsed,
});
```

(merged bar로 조기 return되는 렌더에서는 첫 번째 대입 값('other')이 그대로 유지되어, merged bar
상태에서 벗어나는 전환은 v1에서 애니메이션 대상이 아니게 된다.)

- [ ] **Step 4: getSnapshotBeforeUpdate 추가**

`componentDidUpdate` 바로 위(70행)에 추가:

```ts
getSnapshotBeforeUpdate(
  prevProps: Readonly<SplitViewProps>,
  prevState: Readonly<SplitViewState>,
): { pane: 'first' | 'second'; axis: 'width' | 'height'; from: number } | null {
  const pane = getTransitioningPane(this.prevLayoutMode, this.currentLayoutMode);
  if (pane == null) {
    return null;
  }
  const ref = pane === 'first' ? this.firstPaneRef : this.secondPaneRef;
  const el = ref.current;
  if (el == null) {
    return null;
  }
  const rect = el.getBoundingClientRect();
  const from = this.currentAxis === 'width' ? rect.width : rect.height;
  return { pane, axis: this.currentAxis, from };
}
```

- [ ] **Step 5: componentDidUpdate에 애니메이션 트리거 추가**

기존 `componentDidUpdate`(70~76행)를 아래로 교체:

```ts
componentDidUpdate(
  prevProps: Readonly<SplitViewProps>,
  prevState: Readonly<SplitViewState>,
  snapshot: { pane: 'first' | 'second'; axis: 'width' | 'height'; from: number } | null,
): void {
  if (prevProps.first.ratio !== this.props.first.ratio && prevProps.second.ratio !== this.props.second.ratio) {
    const first = {pos: 0, width: this.props.first.ratio};
    const second = {pos: 0, width: this.props.second.ratio};
    this.setState({first, second});
  }

  if (snapshot != null) {
    const ref = snapshot.pane === 'first' ? this.firstPaneRef : this.secondPaneRef;
    const el = ref.current;
    if (el != null) {
      const rect = el.getBoundingClientRect();
      const to = snapshot.axis === 'width' ? rect.width : rect.height;
      animatePaneResize(el, snapshot.from, to, snapshot.axis, getPrefersReducedMotion());
    }
  }

  this.prevLayoutMode = this.currentLayoutMode;
}
```

- [ ] **Step 6: 두 ReflexElement에 ref 연결**

578행, 633행의 `<ReflexElement`에 각각 `ref` prop 추가:

```tsx
<ReflexElement
  ref={this.firstPaneRef as unknown as React.Ref<InstanceType<typeof ReflexElement>>}
  className={firstPaneClassName}
  minSize={firstMinSize}
  ...
```

```tsx
<ReflexElement
  ref={this.secondPaneRef as unknown as React.Ref<InstanceType<typeof ReflexElement>>}
  className={secondPaneClassName}
  minSize={secondMinSize}
  ...
```

- [ ] **Step 7: 타입/빌드 검증**

Run: `npm run build:test`
Expected: 타입 에러 없이 빌드 성공.

- [ ] **Step 8: 수동 동작 확인**

Run: `npm run dev`, 브라우저에서 2-프레임 페이지를 열어:
1. 한쪽 프레임의 접기 버튼 클릭 → 패널 크기가 420ms 동안 부드럽게 줄어드는지 확인 (즉시 스냅되지 않아야 함).
2. 접힌 상태에서 펼치기 버튼 클릭 → 반대로 부드럽게 늘어나는지 확인.
3. 애니메이션 진행 중 같은 버튼을 다시 클릭 → 처음 크기로 튀지 않고 현재 위치에서 반대 방향으로 이어지는지 확인.
4. 스플리터를 드래그로 리사이즈 → 애니메이션이 개입하지 않고 커서에 즉시 붙는지 확인(회귀 없음).
5. 브라우저/OS의 "동작 줄이기(prefers-reduced-motion)" 설정을 켜고 접기/펼치기 → 즉시 전환되는지 확인.

- [ ] **Step 9: Commit**

```bash
git add src/components/SplitView.tsx
git commit -m "feat: 프레임 한쪽 패널 접힘/펼침에 크기 보간 애니메이션 적용"
```

---

### Task 5: 셰브론 아이콘 교체 → 단일 아이콘 rotate

**Files:**
- Modify: `src/components/frame/FrameHeaderControls.tsx:1,149-158`
- Modify: `src/components/frame/FrameHeaderControls.scss`

**Interfaces:**
- Consumes: 없음
- Produces: 없음 (leaf 컴포넌트, 다른 태스크가 참조하지 않음)

- [ ] **Step 1: import에서 GridCollapse 제거**

`src/components/frame/FrameHeaderControls.tsx:1`을 아래로 교체:

```ts
import { FrameCollapseIcon, FrameExpandIcon, GridExpand, MoveComponentIcon, ActiveMoveComponentIcon } from 'icons/Page';
```

- [ ] **Step 2: 아이콘 교체 로직을 단일 아이콘 + 클래스 토글로 변경**

`src/components/frame/FrameHeaderControls.tsx:149-158`을 아래로 교체:

```tsx
<div
  className={`icon-wrapper chev${isContentCollapsed ? ' is-collapsed' : ''}`}
  role="button"
  tabIndex={0}
  aria-label={isContentCollapsed ? '펴기' : '접기'}
  onClick={handleToggleFrameContentCollapse}
  onKeyDown={handleToggleFrameContentCollapseKeyDown}
>
  <GridExpand/>
</div>
```

- [ ] **Step 3: SCSS에 회전 트랜지션 추가**

`src/components/frame/FrameHeaderControls.scss`의 `.icon-wrapper` 블록(17~24행) 뒤에 추가:

```scss
  .chev svg {
    transition: transform 420ms cubic-bezier(.32, .9, .24, 1);
  }

  .chev.is-collapsed svg {
    transform: rotate(-90deg);
  }

  @media (prefers-reduced-motion: reduce) {
    .chev svg {
      transition: none;
    }
  }
```

- [ ] **Step 4: 빌드 검증**

Run: `npm run build:test`
Expected: 타입 에러/미사용 import 경고 없이 빌드 성공 (GridCollapse import 제거로 인한 미사용 참조 없는지 확인).

- [ ] **Step 5: 수동 동작 확인**

Run: `npm run dev`, 프레임 헤더의 접기/펼치기 아이콘을 클릭:
1. 펼침 상태에서는 아래를 향한 삼각형, 접힘 상태에서는 -90도 회전(오른쪽을 향한 삼각형)으로 보이는지 확인.
2. 클릭 시 아이콘이 깜빡이며 순간 교체되지 않고 부드럽게 회전하는지 확인.

- [ ] **Step 6: Commit**

```bash
git add src/components/frame/FrameHeaderControls.tsx src/components/frame/FrameHeaderControls.scss
git commit -m "feat: 프레임 접기 셰브론을 아이콘 교체 대신 단일 아이콘 회전으로 변경"
```

---

### Task 6: 회귀 확인 (Cypress)

**Files:** 없음 (검증 전용 태스크)

**Interfaces:** 없음

**배경:** 이번 변경 범위(`toggleFrameContentCollapsed`, `SplitView.tsx` 렌더 분기, 프레임 헤더
아이콘)와 겹치는 전용 Cypress spec은 저장소에 없다. 가장 가까운 기존 케이스는
`cypress/e2e/TestCase/Page/EditFramesSplitPos.cy.js`(프레임 분할/크기 조정)와
`cypress/e2e/TestCase/Component/Grid/Basic/FrameExpand.cy.js`(프레임 확대/축소)다.

- [ ] **Step 1: 관련 Cypress 케이스 로컬 실행**

Run: `npx cypress run --spec "cypress/e2e/TestCase/Page/EditFramesSplitPos.cy.js,cypress/e2e/TestCase/Component/Grid/Basic/FrameExpand.cy.js"`
Expected: 두 spec 모두 PASS. 실패하면 이번 변경(특히 Task 4의 ref/생명주기 배선)이 원인인지
`git stash`로 되돌려서 비교 확인한다.

- [ ] **Step 2: 전체 단위 테스트 실행**

Run: `npm run test:run`
Expected: Task 1~3에서 추가한 테스트 포함, 전체 PASS.

- [ ] **Step 3: 최종 빌드 확인**

Run: `npm run build:test`
Expected: 성공.

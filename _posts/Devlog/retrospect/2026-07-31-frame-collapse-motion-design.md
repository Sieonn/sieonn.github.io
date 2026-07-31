# 프레임 접기/펼치기 모션 — 설계 (v1)

- Owner: 임시언 (selim@mirinai.com)
- Status: 설계 승인 대기
- 대상: `grid-service-web` — `SplitView.tsx` / `FrameHeaderControls.tsx`
- 근거 문서: Collapse Motion Spec (사용자 제공 PDF, v0.2, 2026-07-31), Scope: Grid Dashboard · Splitter

## 배경

현재 `SplitView.tsx`에서 프레임(페이지를 H/V split해서 만든 각 패널)을 접거나 펼칠 때
크기(`flex`/`width`/`height`)가 애니메이션 없이 즉시 스냅된다. `Spliter.css`에 있는
`transition: all 1s ease`는 스플리터 hover 피드백용이며 패널 크기 전환과는 무관하다.

사용자가 제공한 Collapse Motion Spec 문서는 별도 프로토타입(`useFlexMotion` 훅,
`ParentSlot`/`SplCell` 컴포넌트) 기준으로 작성되어 있어 이름이 이 코드베이스와 다르다.
이 설계 문서는 스펙의 모션 값과 규칙을 유지하되, 실제 구현은 이 코드베이스의 구조
(`react-reflex` 기반 `SplitView.tsx`, MobX `PageStore`)에 맞춰 새로 설계한다.

## 범위 (v1)

**포함**
- 두 패널 중 한쪽만 접히거나 펼쳐지는 전환 (`firstContentCollapsed` xor
  `secondContentCollapsed`, `SplitView.layout.ts`의 115~134행 분기)에 크기 애니메이션 적용
- 접기/펼치기 토글 아이콘(셰브론) 회전 애니메이션

**제외 (다음 단계로 이관)**
- 양쪽 동시 접힘(equal-width collapsed row), frame expand, merged collapsed bar,
  strip 모드 — 기존처럼 즉시 스냅 유지
- 본문(Frame) 페이드인 — 패널이 펼쳐질 때 새로 mount되는 콘텐츠에 페이드 애니메이션을
  추가하는 작업은 크기 보간과 독립적인 작업이라 v1에서 제외. **Decision (2026-07-31)**:
  사용자 요청으로 다음 단계로 이관.

이 범위 밖 케이스는 현재 동작(즉시 스냅)을 그대로 유지하며 회귀시키지 않는다.

## 모션 토큰

Collapse Motion Spec의 값을 그대로 사용한다. 새 값을 만들지 않는다.

| 토큰 | 값 | 용도 |
|---|---|---|
| `--motion-fold-duration` | `420ms` | 패널 크기 변화 |
| `--motion-fold-ease` | `cubic-bezier(.32,.9,.24,1)` | 패널 크기 변화 이징 |
| `--motion-chevron-duration` | `420ms` | 셰브론 회전 (크기와 동일) |

(`--motion-content-duration`(본문 페이드, 340ms)은 v1 범위 밖이라 이번에 도입하지
않는다. 다음 단계에서 본문 페이드를 구현할 때 함께 추가한다.)

## 아키텍처

### 1. 패널 크기 보간

- `src/components/SplitView.tsx`(클래스 컴포넌트)의 두 `ReflexElement`에 `ref`를
  연결한다. `react-reflex`의 `ReflexElement`는 `React.forwardRef`로 실제 DOM
  `<div>`에 `ref`를 그대로 전달하므로 (`node_modules/react-reflex` 확인 완료)
  라이브러리 내부를 건드릴 필요가 없다.
- `componentDidUpdate`에서 `pageStore.getIsFrameContentCollapsed(frameId)` 값을
  인스턴스 필드(`prevFirstContentCollapsed`/`prevSecondContentCollapsed`)와 비교해
  전환 여부를 감지한다. MobX observer 컴포넌트라 React의 `prevProps`만으로는 상태
  변화를 알 수 없으므로 직접 추적한다.
- 새 유틸 모듈 `src/components/SplitView.motion.ts`에 순수 함수
  `animatePaneResize(el: HTMLElement, from: number, to: number, axis: 'width' | 'height'): void`를 둔다.
  - 진행 중인 애니메이션이 있으면 `cancel()` 전에 현재 렌더 크기를 측정해 새 시작점으로 쓴다.
  - `flexGrow`, `flexShrink`, `minWidth`/`minHeight`(축에 맞게)를 인라인으로 `0`
    잠근다.
  - `el.animate([{ [axis]: from + 'px' }, { [axis]: to + 'px' }], { duration: 420,
    easing: 'cubic-bezier(.32,.9,.24,1)', fill: 'both' })` 호출.
  - `finish` 이벤트에서 인라인 스타일을 원복한다.
  - `window.matchMedia('(prefers-reduced-motion: reduce)').matches`이면 애니메이션
    없이 즉시 최종 상태로 둔다.
  - 목표/시작 크기 차이가 1.5px 미만이면 애니메이션을 생략한다 (스펙 기준).
- 드래그 리사이즈(`onStopResize`)에는 이 로직이 개입하지 않는다 — 트리거는 오직
  `firstContentCollapsed`/`secondContentCollapsed` 값 변화일 때만이다.

### 2. 셰브론 회전

- `src/components/frame/FrameHeaderControls.tsx`의 아이콘 교체 로직
  (`isContentCollapsed ? <GridCollapse/> : <GridExpand/>`, 157행)을 제거하고
  `<GridExpand/>` 하나만 렌더한다.
- `className={`chev${isContentCollapsed ? ' is-collapsed' : ''}`}`로 감싸고
  `FrameHeaderControls.scss`에 회전 트랜지션을 추가한다.

  ```scss
  .chev svg {
    transition: transform var(--motion-chevron-duration) var(--motion-fold-ease);
  }
  .chev.is-collapsed svg {
    transform: rotate(-90deg);
  }
  @media (prefers-reduced-motion: reduce) {
    .chev svg { transition: none; }
  }
  ```

  (확인: `GridExpand`(14×10, 아래 방향 삼각형)와 `GridCollapse`(10×14, 오른쪽 방향
  삼각형)는 동일 도형이 90도 회전된 관계라 시각적으로 자연스럽게 맞아떨어진다.)
- `SplitView.tsx`의 `renderCollapsedBar`/`renderMergedCollapsedBar`가 사용하는
  `GridCollapse`(펴기 아이콘, 항상 고정 표시)는 이번 변경과 무관하므로 그대로 둔다.

## 영향 범위 (blast radius)

| 파일 | 변경 내용 |
|---|---|
| `src/components/SplitView.tsx` | 두 `ReflexElement`에 `ref` 추가, `componentDidUpdate`에 전환 감지·모션 호출 추가 |
| `src/components/SplitView.motion.ts` (신규) | `animatePaneResize` 유틸 |
| `src/components/frame/FrameHeaderControls.tsx` | 아이콘 교체 → 단일 아이콘 + 클래스 토글 |
| `src/components/frame/FrameHeaderControls.scss` | 회전 트랜지션 규칙 추가 |
| CSS 모션 토큰 선언 위치 | `Spliter.css` 또는 `SplitView.scss` 최상단에 `:root`/컨테이너 스코프로 추가 (구현 시 기존 파일 구조 보고 결정) |

`GridCollapse`/`GridExpand`를 사용하는 다른 위치(`PageSetAuth.tsx`)는 별개의
아이콘(`RcTreeGridCollapseIcon`/`RcTreeGridExpandIcon`)을 쓰므로 영향 없음 (확인 완료).

## 테스트

- 단위 테스트(Vitest): `animatePaneResize`가 (a) diff < 1.5px면 애니메이션을 생략하고
  (b) `prefers-reduced-motion` 시 즉시 최종 상태로 두고 (c) 완료 후 인라인 스타일을
  원복하는지 검증.
- Cypress: 프레임 접기/펼치기 관련 기존 케이스가 이번 변경으로 깨지지 않는지
  변경 범위에 해당하는 케이스를 로컬에서 먼저 실행.

## 미해결/확인 필요

- 없음 (v1 범위 관련 질문은 브레인스토밍 단계에서 모두 확인됨).

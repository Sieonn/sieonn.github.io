# 프레임 접기(content collapsed) 개인화 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 프레임 접기(펴기/접기) 상태를 `split_pos`(분할 비율)와 동일한 패턴으로
개인화한다 — 디자인 모드 설정이 기본값, 사용자 모드 토글은 개인화, 페이지 설정
초기화 시 디자인 기본값으로 복원.

**Architecture:** 백엔드 `FrameMaster.is_content_collapsed`(BooleanField, 이미
마이그레이션 완료)를 프론트가 `edit_mode_is_content_collapsed`(디자인 기본값,
프레임별 보관)로 로드 시 복사해두고, 라이브 상태는 기존
`contentCollapsedFrameIds` 배열 + 신규 `FrameInfo.is_content_collapsed` 스칼라
(저장 payload용, 항상 배열과 동기화)로 이중 표현한다. 개인화 값은 기존
`PageUserSettingsStore.settings.frame[id].is_content_collapsed`에 저장하며,
`split_pos`가 쓰는 것과 동일한 로드/저장/초기화 파이프라인을 그대로 탄다.

**Tech Stack:** React 17 + TypeScript, MobX 6, Vitest.

## Global Constraints
- 백엔드 코드는 이 플랜에서 직접 수정하지 않는다 (`gridserviceserver/pagemanager/views.py`
  should_notify 예외, `gridserviceserver/ai/save_manifest.py`,
  `gridserviceserver/ai/save_orchestrator.py` 는 제안만, 코드 변경 없음).
- 서버/개인화/배치 필드명은 `is_content_collapsed`로 통일한다 (백엔드 모델
  필드명과 동일, 변환 계층 없음).
- 이번 범위는 "접기/펴기"(`getIsFrameContentCollapsed`)만 다룬다.
  "확대/전체화면"(`expandedFrameId`)은 건드리지 않는다.
- `moveFrame`(PageStore.tsx line ~4272)에는 접힘 상태 관련 코드를 추가하지
  않는다 (플랜 설계 단계에서 검토 후 제외 확정 — `docs/plan-21968.md` Risks
  참고).
- if/else는 K&R이 아닌 프로젝트 컨벤션(각 `else`를 새 줄에서 시작)을 따른다.
- 커밋 메시지에 Co-Authored-By 트레일러를 넣지 않는다.

---

## Task 1: 저장 페이로드 타입에 `is_content_collapsed` 추가

**Files:**
- Modify: `src/types/DBInterfaces.tsx` (`FrameMaster` line 365-373,
  `FrameSetBatch.ATTRS` line 375-385, `UserSettingsPage.frame` line 973-977)
- Modify: `src/ai-builder/core/saveManifest/pageSaveBody.ts`
  (`FrameMapEntryInput` line 19-27, `FrameBatchEntry.ATTRS` line 38-48,
  `toBatchEntry` line 50-62)
- Modify: `src/ai-builder/core/saveManifest/SaveBundleBuilder.ts`
  (`buildManifestPage` line ~623-632)
- Modify: `src/ai-builder/core/saveManifest/SaveManifest.ts` (매니페스트 프레임
  타입, `split_pos?: number` 근처 line ~141)
- Test: `src/ai-builder/core/saveManifest/pageSaveBody.test.ts`
- Test: `src/ai-builder/core/saveManifest/SaveBundleBuilder.test.ts`

**Interfaces:**
- Produces: `FrameMapEntryInput.is_content_collapsed?: boolean`,
  `FrameBatchEntry['ATTRS']['is_content_collapsed']?: boolean`,
  `toBatchEntry(frame)`가 `ATTRS.is_content_collapsed`에 `frame.is_content_collapsed`를
  매핑. 이후 Task들이 `FrameInfo.is_content_collapsed`를 이 타입과 동일한 이름/
  타입으로 채워 넣는다고 가정한다.

- [ ] **Step 1: 기존 실패하는 테스트부터 갱신 (characterization 깨짐 확인)**

`pageSaveBody.test.ts`의 51-61번 테스트를 아래처럼 바꾼다 (아직 프로덕션 코드는
안 바꾼 상태라 이 시점엔 필드가 없어 실패해야 정상):

```typescript
  it('단일 GRID 메인 프레임 — ACTION=I 하나만 포함한다', () => {
    const mainFrame: MainFramePropsInput = { id: 'f1', type: 'GRID' };
    const frameMap = { f1: frame({ id: 'f1', order: 0 }) };
    const list = buildFrameBatchList(mainFrame, frameMap);
    expect(list).toEqual([
      {
        ACTION: 'I',
        ID: 'f1',
        ATTRS: {
          parent_id: null,
          order: 0,
          frame_type: 'GRID',
          split_orient: undefined,
          split_pos: undefined,
          is_content_collapsed: undefined,
        },
      },
    ]);
  });
```

`SaveBundleBuilder.test.ts`의 140-149번 assertion도 동일하게 바꾼다:

```typescript
    expect(manifest.pages[0].frames).toEqual([
      {
        client_id: 'frame-1',
        parent_client_id: null,
        order: 0,
        frame_type: 'GRID',
        split_orient: undefined,
        split_pos: undefined,
        is_content_collapsed: undefined,
      },
    ]);
```

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `npm run test:run -- pageSaveBody SaveBundleBuilder`
Expected: 두 assertion 모두 FAIL (`is_content_collapsed` 키가 없어서 `toEqual`
불일치)

- [ ] **Step 3: 타입 + 매핑 코드 구현**

`src/types/DBInterfaces.tsx`:

```typescript
export interface FrameMaster {
  id: string;
  parent_id: string | null;
  order: number;
  frame_type: FrameType;
  split_orient: SplitOrientType;
  split_pos: number;
  is_content_collapsed: boolean;
  page: string;
}

export interface FrameSetBatch {
  ACTION: FrameSetBatchActionType;
  ID: string;
  ATTRS: {
    parent_id: string | null,
    order?: number,
    frame_type:FrameType,
    split_orient?: SplitOrientType,
    split_pos?: number,
    is_content_collapsed?: boolean
  };
}
```

`UserSettingsPage.frame`:

```typescript
  frame?: {
    [k: string]: {
      split_pos?: number;
      is_content_collapsed?: boolean;
    }
  },
```

`src/ai-builder/core/saveManifest/pageSaveBody.ts`:

```typescript
export interface FrameMapEntryInput {
  id: string;
  state: DataState;
  parentId: string | null;
  order?: number;
  type: FrameType;
  direction?: SplitOrientType;
  split_pos?: number;
  is_content_collapsed?: boolean;
}
```

```typescript
export interface FrameBatchEntry {
  ACTION: 'I' | 'U' | 'D';
  ID: string;
  ATTRS: {
    parent_id: string | null;
    order?: number;
    frame_type: FrameType;
    split_orient?: SplitOrientType;
    split_pos?: number;
    is_content_collapsed?: boolean;
  };
}
```

```typescript
function toBatchEntry(frame: FrameMapEntryInput): FrameBatchEntry {
  return {
    ACTION: frame.state === DataState.created ? 'I' : frame.state === DataState.deleted ? 'D' : 'U',
    ID: frame.id,
    ATTRS: {
      parent_id: frame.parentId,
      order: frame.order,
      frame_type: frame.type,
      split_orient: frame.direction,
      split_pos: frame.split_pos,
      is_content_collapsed: frame.is_content_collapsed,
    },
  };
}
```

`src/ai-builder/core/saveManifest/SaveBundleBuilder.ts` (`buildManifestPage`):

```typescript
  const frames = frameBatch.map((entry) => ({
    client_id: entry.ID,
    parent_client_id: entry.ATTRS.parent_id,
    order: entry.ATTRS.order,
    frame_type: entry.ATTRS.frame_type,
    split_orient: entry.ATTRS.split_orient,
    split_pos: entry.ATTRS.split_pos,
    is_content_collapsed: entry.ATTRS.is_content_collapsed,
  }));
```

`src/ai-builder/core/saveManifest/SaveManifest.ts`: `split_pos?: number;` 필드
바로 아래에 `is_content_collapsed?: boolean;` 한 줄 추가.

- [ ] **Step 4: 테스트 실행 — 통과 확인**

Run: `npm run test:run -- pageSaveBody SaveBundleBuilder`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/types/DBInterfaces.tsx src/ai-builder/core/saveManifest/pageSaveBody.ts src/ai-builder/core/saveManifest/pageSaveBody.test.ts src/ai-builder/core/saveManifest/SaveBundleBuilder.ts src/ai-builder/core/saveManifest/SaveBundleBuilder.test.ts src/ai-builder/core/saveManifest/SaveManifest.ts
git commit -m "feat(frame): 저장 페이로드/매니페스트에 is_content_collapsed 필드 추가"
```

---

## Task 2: `FrameInfo`에 접힘 상태 필드 추가

**Files:**
- Modify: `src/components/Frame.tsx` (`FrameInfo` line 43-55)

**Interfaces:**
- Consumes: 없음 (신규 타입 필드)
- Produces: `FrameInfo.is_content_collapsed?: boolean` (라이브 값,
  `contentCollapsedFrameIds`와 항상 동기화되어야 하는 저장용 스칼라),
  `FrameInfo.edit_mode_is_content_collapsed?: boolean` (디자인 모드 기본값,
  `edit_mode_split_pos`와 동일 역할). 이후 모든 Task가 이 두 필드명을 그대로
  사용한다.

- [ ] **Step 1: 타입 추가**

```typescript
export interface FrameInfo {
  componentId?: string;
  componentType?: GridType;
  direction?: SplitOrientType;
  id: string;
  isContentCollapsed?: boolean;
  order?: number;
  parentId: string | null;
  type: FrameType;
  state: DataState;
  split_pos?: number;
  edit_mode_split_pos?: number;
  is_content_collapsed?: boolean;
  edit_mode_is_content_collapsed?: boolean;
}
```

(기존 `isContentCollapsed?: boolean`는 어디서도 읽고 쓰지 않는 죽은 필드이므로
그대로 둔다 — 이번 작업 범위와 무관한 정리이므로 건드리지 않는다.)

- [ ] **Step 2: 타입만 추가하는 변경이므로 빌드로 검증**

Run: `npm run build:test`
Expected: 타입 에러 없이 빌드 성공 (아직 이 필드를 쓰는 코드가 없으므로 unused
경고 정도만 있을 수 있음)

- [ ] **Step 3: Commit**

```bash
git add src/components/Frame.tsx
git commit -m "feat(frame): FrameInfo에 접힘 상태 라이브/디자인기본값 필드 추가"
```

---

## Task 3: `setFrameContentCollapsed`가 `is_content_collapsed`를 동기화

**Files:**
- Modify: `src/components/store/PageStore.tsx` (`setFrameContentCollapsed`
  line 1036-1058)
- Test: `src/components/store/PageStore.contentCollapsed.test.ts` (신규)

**Interfaces:**
- Consumes: `FrameInfo.is_content_collapsed`(Task 2)
- Produces: `setFrameContentCollapsed(frameId, collapsed)` 호출 후
  `frame.is_content_collapsed === collapsed`가 항상 성립한다는 불변조건. 이후
  Task 4~8이 이 불변조건에 의존한다.

- [ ] **Step 1: 실패하는 테스트 작성**

`src/components/store/PageStore.contentCollapsed.test.ts` 신규 생성:

```typescript
import { describe, it, expect, beforeEach, vi } from 'vitest';

vi.mock('../api/ServerAPI', () => ({
  default: { get: vi.fn(), post: vi.fn(), put: vi.fn(), delete: vi.fn(), patch: vi.fn() },
}));
vi.mock('../../runtimeConfig', () => ({
  getRuntimeConfigSync: () => ({ baseApiUrl: 'http://localhost/api' }),
}));
vi.mock('../Frame', () => ({}));
vi.mock('react-lottie', () => ({ default: () => null }));
vi.mock('../grid/GridManager', () => ({
  GridManager: class {},
  BaseGridWrapper: class {},
}));
vi.mock('../chart/ChartManager', () => ({ default: class {} }));
vi.mock('../form/FormManager', () => ({ default: class {} }));
vi.mock('../graph/calendar/CalendarManager', () => ({ default: class {} }));
vi.mock('../graph/timeline/TimelineManager', () => ({ default: class {} }));

import { PageStore } from './PageStore';
import { DataState } from '../../types/State';
import type { FrameInfo } from '../Frame';

function makeRootStore() {
  return {} as any;
}

function frame(overrides: Partial<FrameInfo> & { id: string; parentId: string | null }): FrameInfo {
  return {
    type: 'GRID',
    state: DataState.none,
    order: 1,
    ...overrides,
  } as FrameInfo;
}

describe('PageStore.setFrameContentCollapsed — is_content_collapsed 스칼라 동기화', () => {
  let store: PageStore;

  beforeEach(() => {
    store = new PageStore(makeRootStore());
  });

  it('collapsed=true로 설정하면 contentCollapsedFrameIds와 frame.is_content_collapsed가 함께 true가 된다', () => {
    store.frameMap = { f1: frame({ id: 'f1', parentId: null }) };

    store.setFrameContentCollapsed('f1', true);

    expect(store.contentCollapsedFrameIds).toEqual(['f1']);
    expect(store.frameMap['f1'].is_content_collapsed).toBe(true);
  });

  it('collapsed=false로 되돌리면 둘 다 false/제거된다', () => {
    store.frameMap = { f1: frame({ id: 'f1', parentId: null }) };
    store.setFrameContentCollapsed('f1', true);

    store.setFrameContentCollapsed('f1', false);

    expect(store.contentCollapsedFrameIds).toEqual([]);
    expect(store.frameMap['f1'].is_content_collapsed).toBe(false);
  });
});
```

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: FAIL (`frame.is_content_collapsed`가 `undefined`)

- [ ] **Step 3: 최소 구현**

`PageStore.tsx`의 `setFrameContentCollapsed`를 아래로 교체:

```typescript
  @action
  public setFrameContentCollapsed(frameId: string, collapsed: boolean) {
    const normalizedFrameId = String(frameId);
    if (this.getIsFrameContentCollapsed(normalizedFrameId) === collapsed) {
      return;
    }
    const frame = this.getFrame(normalizedFrameId);
    if (frame == null) {
      return;
    }
    if (collapsed) {
      if (!this.contentCollapsedFrameIds.includes(normalizedFrameId)) {
        this.contentCollapsedFrameIds.push(normalizedFrameId);
      }
      if (this.getIsFrameExpanded(normalizedFrameId)) {
        this.expandedFrameId = null;
      }
    }
    else {
      this.contentCollapsedFrameIds = this.contentCollapsedFrameIds.filter(
        (id) => id !== normalizedFrameId
      );
    }
    frame.is_content_collapsed = collapsed;
  }
```

(변경점: `this.getFrame(normalizedFrameId) == null` 조기 return을 `frame` 변수로
받아 재사용하도록 바꾸고, 마지막에 `frame.is_content_collapsed = collapsed`를
추가했다. 동작 분기 로직 자체는 그대로다.)

- [ ] **Step 4: 테스트 실행 — 통과 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/components/store/PageStore.tsx src/components/store/PageStore.contentCollapsed.test.ts
git commit -m "feat(frame): setFrameContentCollapsed가 is_content_collapsed 스칼라도 동기화"
```

---

## Task 4: 페이지 로드 시 디자인 기본값/개인화 시딩

**Files:**
- Modify: `src/components/store/PageStore.tsx` (로드 블록 line ~3538-3589)
- Test: `src/components/store/PageStore.contentCollapsed.test.ts` (Task 3에서
  만든 파일에 케이스 추가)

**Interfaces:**
- Consumes: `setFrameContentCollapsed`(Task 3),
  `userSettings.settings.frame[id].is_content_collapsed`(기존
  `PageUserSettingsStore` 구조, 타입은 Task 1에서 추가)
- Produces: 페이지 로드 완료 후 각 프레임의 `edit_mode_is_content_collapsed`가
  서버 값과 같고, `contentCollapsedFrameIds`/`is_content_collapsed`가 개인화
  값(있으면) 또는 디자인 기본값(없으면)과 같다는 불변조건. Task 7/8이 이 로드
  결과를 전제로 한다.

**참고:** 로드 로직은 `PageStore.tsx`에서 직접 HTTP 요청 성공 콜백 내부에
있어 단위 테스트로 그 경로 전체를 태우기보다, 이 블록이 하는 일과 동일한 모양의
프레임 구성 로직을 별도 테스트에서 **`frameMap`을 직접 구성한 뒤
`setFrameContentCollapsed`/필드 대입 순서를 재현**해서 검증한다(아래 테스트는
로드 이후 도달하는 "상태"를 검증하는 것이지 HTTP 콜백 자체를 실행하지 않는다 —
기존 `PageStore.moveFrame.test.ts`류도 HTTP 콜백을 통째로 태우지 않고 상태
전이만 검증하는 스타일을 따른다).

- [ ] **Step 1: 실패하는 테스트 작성**

`PageStore.contentCollapsed.test.ts`에 새 `describe` 블록 추가:

```typescript
describe('PageStore 페이지 로드 — 접힘 상태 기본값/개인화 시딩', () => {
  let store: PageStore;

  beforeEach(() => {
    store = new PageStore(makeRootStore());
  });

  it('개인화 값이 없으면 서버(디자인) 기본값으로 시딩된다', () => {
    store.frameMap = {
      f1: frame({ id: 'f1', parentId: null, edit_mode_is_content_collapsed: true }),
    };

    Object.values(store.frameMap).forEach((f) => {
      const personalized = (store.userSettings.settings.frame as any)?.[f.id]?.is_content_collapsed;
      const initial = personalized != null ? personalized : f.edit_mode_is_content_collapsed;
      if (initial) {
        store.setFrameContentCollapsed(f.id, true);
      }
    });

    expect(store.getIsFrameContentCollapsed('f1')).toBe(true);
    expect(store.frameMap['f1'].is_content_collapsed).toBe(true);
  });

  it('개인화 값이 있으면 디자인 기본값 대신 개인화 값을 쓴다', () => {
    store.frameMap = {
      f1: frame({ id: 'f1', parentId: null, edit_mode_is_content_collapsed: true }),
    };
    (store.userSettings.settings as any).frame = { f1: { is_content_collapsed: false } };

    Object.values(store.frameMap).forEach((f) => {
      const personalized = (store.userSettings.settings.frame as any)?.[f.id]?.is_content_collapsed;
      const initial = personalized != null ? personalized : f.edit_mode_is_content_collapsed;
      if (initial) {
        store.setFrameContentCollapsed(f.id, true);
      }
    });

    expect(store.getIsFrameContentCollapsed('f1')).toBe(false);
  });
});
```

이 테스트는 "로드 블록에 넣을 시딩 로직"을 그대로 인라인으로 재현해 먼저
검증하는 것이다 — 실제 구현(Step 3)에서 동일한 로직을 로드 블록 안에 넣는다.

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: 새 테스트 2개 모두 FAIL — `store.userSettings`가 아직 없거나
(`PageUserSettings` 기본 인스턴스라 `settings.frame`이 `undefined`) 첫 번째
테스트는 시딩 로직 자체는 인라인으로 넣었으니 이 시점엔 사실 통과할 수 있다.
**만약 두 테스트가 이미 통과한다면 이 Step은 "로직 자체는 맞다"는 확인으로
간주하고, Step 3에서 이 로직을 실제 로드 블록에 옮겨 심는 작업에 집중한다.**

- [ ] **Step 3: 로드 블록에 동일 로직 이식**

`PageStore.tsx`의 프레임 로드 루프(line ~3538) 안, `frameMap[frame.id] = {...}`
대입 직후에 `edit_mode_is_content_collapsed` 필드를 추가하고, 루프가 끝난 뒤
시딩 pass를 추가한다.

`INNER`/그 외 분기 양쪽의 객체 리터럴에 필드 추가:

```typescript
            if (frame.frame_type === 'INNER') {
              frameMap[frame.id] = {
                direction:
                  frame.split_orient === 'H'
                    ? SplitOrientType.horizontal
                    : SplitOrientType.vertical,
                id: frame.id,
                order: frame.order,
                parentId: frame.parent_id,
                type: 'INNER',
                state: DataState.none,
                split_pos: splitPos,
                edit_mode_split_pos: frame.split_pos,
                edit_mode_is_content_collapsed: frame.is_content_collapsed,
              };
            } else {
              frameMap[frame.id] = {
                id: frame.id,
                order: frame.order,
                parentId: frame.parent_id,
                type: frame.frame_type,
                state: DataState.none,
                split_pos: splitPos,
                edit_mode_split_pos: frame.split_pos,
                edit_mode_is_content_collapsed: frame.is_content_collapsed,
              };
```

`for` 루프가 끝나는 지점(`this.frameMap = frameMap;`가 대입되는 곳 — 루프
직후) 바로 다음에 시딩 pass 추가:

```typescript
          Object.values(frameMap).forEach((f: FrameInfo) => {
            const personalized = this.userSettings.settings.frame?.[f.id]?.is_content_collapsed;
            const shouldCollapse = personalized != null ? personalized : f.edit_mode_is_content_collapsed;
            if (shouldCollapse) {
              this.setFrameContentCollapsed(f.id, true);
            }
          });
```

(`this.frameMap = frameMap;` 대입이 먼저 이뤄져야 `setFrameContentCollapsed`
내부의 `this.getFrame(id)`가 프레임을 찾을 수 있다 — 대입 순서를 반드시
확인한다.)

- [ ] **Step 4: 테스트 실행 — 통과 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/components/store/PageStore.tsx src/components/store/PageStore.contentCollapsed.test.ts
git commit -m "feat(frame): 페이지 로드 시 접힘 상태 디자인기본값/개인화 시딩"
```

---

## Task 5: 공개(퍼블릭) 페이지 로더도 `split_pos`와 동일하게 반영

**Files:**
- Modify: `src/components/store/PageStore.tsx` (공개 페이지 로더, frame 생성
  블록 line ~3968-3989, `this.frameMap = frameMap;` 대입 지점 line ~4078)
- Test: `src/components/store/PageStore.contentCollapsed.test.ts`

**Interfaces:**
- Consumes: `setFrameContentCollapsed`(Task 3)
- Produces: 공개 페이지 로드 후 `getIsFrameContentCollapsed(id) ===
  !!frame.is_content_collapsed` (개인화·edit_mode 개념 없이 서버 값을 그대로
  반영— `split_pos`가 이 로더에서 `edit_mode_split_pos`/개인화 없이 서버 값을
  그대로 쓰는 것과 동일).

**참고:** 공개 페이지는 로그인/개인화가 없는 뷰 전용 경로라 `edit_mode_is_content_collapsed`나
`userSettings` 조회는 필요 없다. `split_pos`가 이 로더에서 `frameMap[frame.id] =
{ ..., split_pos: frame.split_pos }`로 서버 값을 그대로 대입하고 끝내는 것과
동일하게, `is_content_collapsed`도 그 자리에 나란히 대입하고, `contentCollapsedFrameIds`
배열만 로드 완료 시점에 한 번 시딩한다.

- [ ] **Step 1: 실패하는 테스트 작성**

`PageStore.contentCollapsed.test.ts`에 추가:

```typescript
describe('PageStore 공개 페이지 로드 — 접힘 상태를 서버 값 그대로 반영', () => {
  let store: PageStore;

  beforeEach(() => {
    store = new PageStore(makeRootStore());
  });

  it('개인화/edit_mode 없이 서버 is_content_collapsed 값을 그대로 적용한다', () => {
    const frameMap = {
      f1: frame({ id: 'f1', parentId: null, is_content_collapsed: true }),
    };
    store.frameMap = frameMap;

    Object.values(store.frameMap).forEach((f) => {
      if (f.is_content_collapsed) {
        store.setFrameContentCollapsed(f.id, true);
      }
    });

    expect(store.getIsFrameContentCollapsed('f1')).toBe(true);
  });
});
```

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: 이 테스트는 로직을 인라인으로 그대로 재현했으므로 이미 통과할 수
있다 — Task 3이 끝난 시점이라면 PASS도 정상이다. 이 경우 Step 1의 로직을 그대로
Step 3에서 실제 로더 코드에 이식하는 데 집중한다.

- [ ] **Step 3: 공개 페이지 로더에 이식**

frame 생성 블록(line ~3968-3989) 양쪽 분기에 `split_pos: frame.split_pos` 옆에
한 줄 추가:

```typescript
          if (frame.frame_type === 'INNER') {
            frameMap[frame.id] = {
              direction:
                frame.split_orient === 'H'
                  ? SplitOrientType.horizontal
                  : SplitOrientType.vertical,
              id: frame.id,
              order: frame.order,
              parentId: frame.parent_id,
              type: 'INNER',
              state: DataState.none,
              split_pos: frame.split_pos,
              is_content_collapsed: frame.is_content_collapsed,
            };
          } else {
            frameMap[frame.id] = {
              id: frame.id,
              order: frame.order,
              parentId: frame.parent_id,
              type: frame.frame_type,
              state: DataState.none,
              split_pos: frame.split_pos,
              is_content_collapsed: frame.is_content_collapsed,
            };
```

`this.frameMap = frameMap;` 대입(line ~4078) 바로 다음 줄에 시딩 pass 추가:

```typescript
        this.frameMap = frameMap;
        Object.values(frameMap).forEach((f: FrameInfo) => {
          if (f.is_content_collapsed) {
            this.setFrameContentCollapsed(f.id, true);
          }
        });
```

- [ ] **Step 4: 테스트 실행 — 통과 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/components/store/PageStore.tsx src/components/store/PageStore.contentCollapsed.test.ts
git commit -m "feat(frame): 공개 페이지 로더에도 접힘 상태를 split_pos와 동일하게 반영"
```

---

## Task 6: `toggleFrameContentCollapsed` 모드 분기 — edit는 디자인 상태, view는 개인화

**Files:**
- Modify: `src/components/store/PageStore.tsx` (`toggleFrameContentCollapsed`
  line ~1059-1078)
- Test: `src/components/store/PageStore.contentCollapsed.test.ts`

**Interfaces:**
- Consumes: `setFrameContentCollapsed`(Task 3),
  `this.userSettings.setSettingFrameRelated(frameId, propertyName, value,
  send?)`(기존 메서드, 시그니처 변경 없음)
- Produces: edit 모드에서 토글 시 `frame.state === DataState.updated`(단,
  `created`/이미 `updated`면 유지), view 모드에서 토글 시
  `userSettings.settings.frame[id].is_content_collapsed === (토글 후 값)`.

- [ ] **Step 1: 실패하는 테스트 작성**

```typescript
import { PageMode } from './PageStore';

describe('PageStore.toggleFrameContentCollapsed — 모드별 분기', () => {
  let store: PageStore;

  beforeEach(() => {
    store = new PageStore(makeRootStore());
  });

  it('edit 모드에서 토글하면 frame.state가 updated로 바뀐다 (개인화는 저장하지 않는다)', () => {
    store.frameMap = { f1: frame({ id: 'f1', parentId: null, state: DataState.none }) };
    store.mode = PageMode.edit;
    const spy = vi.spyOn(store.userSettings, 'setSettingFrameRelated');

    store.toggleFrameContentCollapsed('f1');

    expect(store.frameMap['f1'].state).toBe(DataState.updated);
    expect(store.getIsFrameContentCollapsed('f1')).toBe(true);
    expect(spy).not.toHaveBeenCalled();
  });

  it('edit 모드에서 이미 created 상태면 created를 유지한다', () => {
    store.frameMap = { f1: frame({ id: 'f1', parentId: null, state: DataState.created }) };
    store.mode = PageMode.edit;

    store.toggleFrameContentCollapsed('f1');

    expect(store.frameMap['f1'].state).toBe(DataState.created);
  });

  it('view 모드에서 토글하면 개인화 설정에 저장되고 frame.state는 바뀌지 않는다', () => {
    store.frameMap = { f1: frame({ id: 'f1', parentId: null, state: DataState.none }) };
    store.mode = PageMode.view;
    const spy = vi.spyOn(store.userSettings, 'setSettingFrameRelated').mockImplementation(() => {});

    store.toggleFrameContentCollapsed('f1');

    expect(spy).toHaveBeenCalledWith('f1', 'is_content_collapsed', true);
    expect(store.frameMap['f1'].state).toBe(DataState.none);
  });
});
```

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: 위 3개 테스트 FAIL (모드 분기 코드가 아직 없음)

- [ ] **Step 3: 구현**

`toggleFrameContentCollapsed`를 아래로 교체:

```typescript
  @action
  public toggleFrameContentCollapsed(frameId: string) {
    const normalizedFrameId = String(frameId);
    const frame = this.getFrame(normalizedFrameId);
    if (frame == null) {
      return;
    }
    const shouldCollapse = !this.getIsFrameContentCollapsed(normalizedFrameId);
    this.setFrameContentCollapsed(normalizedFrameId, shouldCollapse);
    if (this.mode === PageMode.edit) {
      if (!(frame.state === DataState.created || frame.state === DataState.updated)) {
        frame.state = DataState.updated;
      }
    }
    else {
      this.userSettings.setSettingFrameRelated(normalizedFrameId, 'is_content_collapsed', shouldCollapse);
    }
    if (frame.type === 'GRAPH' && frame.componentId != null) {
      const chartManager = this.chartManager[frame.componentId];
      if (chartManager != null) {
        chartManager.RefreshGraph();
      }
    }
    setTimeout(() => {
      window.dispatchEvent(new Event('resize'));
      this.gridManager.resizeAll();
    }, 1);
  }
```

(`setFrameSplitPos`의 edit 모드 state 마킹 조건을 그대로 가져왔다: `created`나
이미 `updated`면 건드리지 않고, 그 외에만 `updated`로 바꾼다.)

- [ ] **Step 4: 테스트 실행 — 통과 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/components/store/PageStore.tsx src/components/store/PageStore.contentCollapsed.test.ts
git commit -m "feat(frame): toggleFrameContentCollapsed가 edit/view 모드에 따라 디자인기본값 또는 개인화를 갱신"
```

---

## Task 7: `setPageEditMode` 진입 시 디자인 기본값 강제 동기화

**Files:**
- Modify: `src/components/store/PageStore.tsx` (`setPageEditMode` line
  ~3275-3320)
- Test: `src/components/store/PageStore.contentCollapsed.test.ts`

**Interfaces:**
- Consumes: `setFrameContentCollapsed`(Task 3)
- Produces: `setPageEditMode()` 호출 후 (강제 저장 다이얼로그 경로를 타지 않는
  한) 모든 프레임의 `getIsFrameContentCollapsed(id) ===
  !!frame.edit_mode_is_content_collapsed`.

- [ ] **Step 1: 실패하는 테스트 작성**

```typescript
describe('PageStore.setPageEditMode — 접힘 상태를 디자인 기본값으로 강제 동기화', () => {
  let store: PageStore;

  beforeEach(() => {
    store = new PageStore(makeRootStore());
    vi.spyOn(store, 'hasPageModifiablePermission', 'get').mockReturnValue(true);
    vi.spyOn(store, 'checkHavingUnsavedData').mockReturnValue(false);
    vi.spyOn(store, 'checkHasErrorSavingPage').mockImplementation(() => {});
  });

  it('개인화로 펴져 있어도(view에서 접힘=false) 디자인 기본값(true)으로 되돌린다', () => {
    store.frameMap = {
      f1: frame({ id: 'f1', parentId: null, edit_mode_is_content_collapsed: true }),
    };
    // view 모드에서 사용자가 펴둔 상태를 흉내
    store.contentCollapsedFrameIds = [];

    store.setPageEditMode(true);

    expect(store.getIsFrameContentCollapsed('f1')).toBe(true);
  });

  it('디자인 기본값이 접힘이 아니면(false/undefined) 개인화로 접혀 있던 것도 편다', () => {
    store.frameMap = {
      f1: frame({ id: 'f1', parentId: null, edit_mode_is_content_collapsed: false }),
    };
    store.contentCollapsedFrameIds = ['f1'];
    store.frameMap['f1'].is_content_collapsed = true;

    store.setPageEditMode(true);

    expect(store.getIsFrameContentCollapsed('f1')).toBe(false);
  });
});
```

(`hasPageModifiablePermission`은 getter라 `vi.spyOn(obj, 'prop', 'get')` 형태로
스텁한다 — vitest/jest 공통 패턴.)

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: FAIL (아직 collapse 동기화 코드가 없음)

- [ ] **Step 3: 구현**

`setPageEditMode`의 기존 `split_pos` 동기화 루프(line ~3280-3290) 바로 안,
`edit_mode_split_pos` 동기화 줄 다음에 한 줄 추가:

```typescript
    const frameIdList = Object.keys(this.frameMap); // 화면 비율 디자인 모드에서 설정했으면 변경되도록
    let gridIdList:string[] = [];
    for (let id of frameIdList) {
      if (this.frameMap[id].edit_mode_split_pos != null && this.frameMap[id].split_pos !== this.frameMap[id].edit_mode_split_pos) {
        this.frameMap[id].split_pos = this.frameMap[id].edit_mode_split_pos;
      }
      if (this.getIsFrameContentCollapsed(id) !== !!this.frameMap[id].edit_mode_is_content_collapsed) {
        this.setFrameContentCollapsed(id, !!this.frameMap[id].edit_mode_is_content_collapsed);
      }
      const frame = this.frameMap[id];
      if (frame != null && frame.type === 'GRID' && frame.componentId != null && typeof frame.componentId === 'string') {
        gridIdList.push(frame.componentId);
      }
    }
```

- [ ] **Step 4: 테스트 실행 — 통과 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/components/store/PageStore.tsx src/components/store/PageStore.contentCollapsed.test.ts
git commit -m "feat(frame): edit 모드 진입 시 접힘 상태를 디자인 기본값으로 강제 동기화"
```

---

## Task 8: `cancelPageEditing` 시 개인화 복원 (`restoreFrameContentCollapsedStates`)

**Files:**
- Modify: `src/components/store/PageStore.tsx` (`restoreFrameSplitPositions`
  옆에 신규 `restoreFrameContentCollapsedStates` 추가, line ~3386 부근;
  `cancelPageEditing` line 550, 576-585의 두 호출 지점)
- Test: `src/components/store/PageStore.contentCollapsed.test.ts`

**Interfaces:**
- Consumes: `setFrameContentCollapsed`(Task 3)
- Produces: `restoreFrameContentCollapsedStates()` — private 메서드,
  `cancelPageEditing`이 `frameMap`을 `originalFrameMap`으로 되돌린 직후 호출해
  개인화 값을 다시 입힌다.

- [ ] **Step 1: 실패하는 테스트 작성**

```typescript
describe('PageStore.cancelPageEditing — 접힘 상태 개인화 복원', () => {
  let store: PageStore;

  beforeEach(() => {
    store = new PageStore(makeRootStore());
  });

  it('edit 모드 취소 시 개인화된 접힘 값이 있으면 그 값으로 복원한다', () => {
    const f1 = frame({ id: 'f1', parentId: null, edit_mode_is_content_collapsed: false });
    store.frameMap = { f1 };
    store.originalFrameMap = { f1: { ...f1 } };
    (store.userSettings.settings as any).frame = { f1: { is_content_collapsed: true } };
    vi.spyOn(store, 'checkHavingChangeFrameData').mockReturnValue(false);

    (store as any).cancelPageEditing();

    expect(store.getIsFrameContentCollapsed('f1')).toBe(true);
  });
});
```

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: FAIL (`restoreFrameContentCollapsedStates`가 없어 복원되지 않음 —
`getIsFrameContentCollapsed('f1')`이 `false`로 남음)

- [ ] **Step 3: 구현**

`restoreFrameSplitPositions` 바로 아래에 새 private 메서드 추가:

```typescript
  /**
   * 프레임 사용자 세팅 접힘 상태를 복원합니다
   * @private
   */
  private restoreFrameContentCollapsedStates() {
    const frameIdList = Object.keys(this.frameMap);
    for (let id of frameIdList) {
      const frame = this.frameMap[id];
      if (frame == null) {
        continue;
      }
      const personalized = this.userSettings.settings?.frame?.[id]?.is_content_collapsed;
      if (personalized != null && personalized !== this.getIsFrameContentCollapsed(id)) {
        this.setFrameContentCollapsed(id, personalized);
      }
    }
  }
```

`cancelPageEditing`의 두 호출 지점(line 555, 580)에 나란히 호출 추가:

```typescript
      if (!this.checkHavingChangeFrameData()) {
        this.frameMap = cloneDeep(this.originalFrameMap);
        this.restoreFrameSplitPositions();
        this.restoreFrameContentCollapsedStates();
      }
```

```typescript
        if (this.checkHavingChangeFrameData()) {
          this.setUnsavedFrameDataCallback(() => {
            if (this.clickProcess === 'cancel') {
              this.frameMap = cloneDeep(this.originalFrameMap);
              this.restoreFrameSplitPositions();
              this.restoreFrameContentCollapsedStates();
              this.executeCancelLogic();
            }
            this.handleHomeButtonNavigation()
          })
        }
```

- [ ] **Step 4: 테스트 실행 — 통과 확인**

Run: `npm run test:run -- PageStore.contentCollapsed`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/components/store/PageStore.tsx src/components/store/PageStore.contentCollapsed.test.ts
git commit -m "feat(frame): edit 모드 취소 시 접힘 상태 개인화 복원"
```

---

## Task 9: `PageUserSettingsStore.allSettingReset`에 접힘 상태 복원 추가

**Files:**
- Modify: `src/components/store/PageUserSettingsStore.tsx`
  (`allSettingReset` line ~324-335, `split_pos` 복원 루프 옆)
- Test: `src/components/store/PageUserSettingsStore.contentCollapsedReset.test.ts`
  (신규)

**Interfaces:**
- Consumes: `PageStore.setFrameContentCollapsed`(Task 3),
  `FrameInfo.edit_mode_is_content_collapsed`/`is_content_collapsed`(Task 2)
- Produces: `allSettingReset()` 호출 후, 개인화로 디자인 기본값과 달라져 있던
  모든 프레임의 접힘 상태가 디자인 기본값으로 되돌아간다는 불변조건.

- [ ] **Step 1: 실패하는 테스트 작성**

`src/components/store/PageUserSettingsStore.contentCollapsedReset.test.ts` 신규
생성 (`PageUserSettingsStore.timelineStyleCount.test.ts`의 mock 패턴을 그대로
따름):

```typescript
import { describe, it, expect, beforeEach, vi } from 'vitest';

vi.mock('../api/ServerAPI', () => ({
  default: { get: vi.fn(), post: vi.fn(), put: vi.fn(), delete: vi.fn() },
}));
vi.mock('components/grid/GridManager', () => ({
  GridManager: class {},
  BaseGridWrapper: class {},
  DEFAULT_GRID_SETTING: {},
}));
vi.mock('components/graph/timeline/TimelineManager', () => ({
  default: class {},
  DEFAULT_STEP: 1,
}));

import PageUserSettings from './PageUserSettingsStore';

describe('PageUserSettingsStore.allSettingReset — 접힘 상태 개인화 복원', () => {
  let settings: PageUserSettings;
  let setFrameContentCollapsed: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    settings = new PageUserSettings();
    setFrameContentCollapsed = vi.fn();
    (settings as any).pageStore = {
      frameMap: {
        f1: {
          id: 'f1',
          is_content_collapsed: true,
          edit_mode_is_content_collapsed: false,
        },
        f2: {
          id: 'f2',
          is_content_collapsed: false,
          edit_mode_is_content_collapsed: false,
        },
      },
      calendarManager: {},
      chartManager: {},
      timelineManager: {},
      isPublic: true,
      setFrameContentCollapsed,
      setFrameSplitPos: vi.fn(),
    };
  });

  it('개인화로 디자인 기본값과 달라진 프레임만 setFrameContentCollapsed로 되돌린다', () => {
    settings.allSettingReset();

    expect(setFrameContentCollapsed).toHaveBeenCalledWith('f1', false);
    expect(setFrameContentCollapsed).not.toHaveBeenCalledWith('f2', expect.anything());
  });
});
```

- [ ] **Step 2: 테스트 실행 — 실패 확인**

Run: `npm run test:run -- PageUserSettingsStore.contentCollapsedReset`
Expected: FAIL (`setFrameContentCollapsed`가 호출되지 않음)

- [ ] **Step 3: 구현**

`allSettingReset` 안, 기존 `split_pos` 복원 루프 바로 아래에 추가:

```typescript
    // 프레임
    const frameMap = this.pageStore.frameMap;
    Object.values(frameMap).forEach(frame => {
      if (
        frame != null &&
        frame.split_pos != null &&
        frame.edit_mode_split_pos != null &&
        frame.split_pos !== frame.edit_mode_split_pos
      ) {
        this.pageStore.setFrameSplitPos(frame.id, frame.edit_mode_split_pos);
      }
      if (
        frame != null &&
        frame.is_content_collapsed !== !!frame.edit_mode_is_content_collapsed
      ) {
        this.pageStore.setFrameContentCollapsed(frame.id, !!frame.edit_mode_is_content_collapsed);
      }
    });
```

- [ ] **Step 4: 테스트 실행 — 통과 확인**

Run: `npm run test:run -- PageUserSettingsStore.contentCollapsedReset`
Expected: PASS

- [ ] **Step 5: 기존 관련 테스트 회귀 확인**

Run: `npm run test:run -- PageUserSettingsStore`
Expected: 기존 `PageUserSettingsStore.timelineStyleCount.test.ts` 포함 전부 PASS

- [ ] **Step 6: Commit**

```bash
git add src/components/store/PageUserSettingsStore.tsx src/components/store/PageUserSettingsStore.contentCollapsedReset.test.ts
git commit -m "feat(frame): 페이지 설정 초기화 시 접힘 상태도 디자인 기본값으로 복원"
```

---

## Task 10: 전체 빌드 검증 + 수동 QA

**Files:**
- 없음 (검증 전용 태스크)

**Interfaces:**
- Consumes: Task 1~8의 모든 변경
- Produces: 없음 (완료 신호)

- [ ] **Step 1: 전체 단위 테스트 실행**

Run: `npm run test:run`
Expected: 전체 PASS (회귀 없음)

- [ ] **Step 2: 빌드 검증**

Run: `npm run build:test`
Expected: 타입 에러 없이 빌드 성공

- [ ] **Step 3: 수동 QA (dev 서버)**

Run: `npm run dev`, 브라우저에서:
1. 멀티프레임 페이지를 edit 모드로 열고, 프레임 하나를 접은 뒤 저장한다.
2. view 모드로 돌아와 새로고침 — 접힌 상태가 유지되는지 확인(디자인 기본값
   반영).
3. view 모드에서 그 프레임을 펴본다 — 새로고침해도 편 상태가 유지되는지
   확인(개인화 저장).
4. 페이지 설정 초기화를 실행 — 다시 접힌 상태(디자인 기본값)로 돌아오는지
   확인.
5. edit 모드로 다시 들어가서 — 개인화(펴짐)와 무관하게 디자인 기본값(접힘)이
   보이는지 확인.

Expected: 위 5개 시나리오 모두 기대대로 동작.

- [ ] **Step 4: Commit (필요 시)**

QA 중 수정 사항이 있었다면 해당 커밋을 생성한다. 없으면 이 Task는 커밋 없이
종료.

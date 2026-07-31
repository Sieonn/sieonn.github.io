# 집계 푸터 클릭 영역 확장 및 위젯 버튼 상시 노출 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 일반 컬럼 집계 푸터(`GridColumnFooterCell`)는 셀 영역 전체를 클릭해도 집계 타입
드롭다운이 열리게 하고, 선택 영역 집계 위젯의 펼침 버튼(`.encke-grid-select-aggregate-widget-btn`)은
hover 없이 항상 아이콘이 보이게 한다.

**Architecture:** 두 변경 모두 기존 코드에 국소적으로 추가/수정한다. 새 파일이나 새 추상화는
만들지 않는다. `GridCell.js`에서는 기존에 `menuIcon`에만 걸려 있던 클릭 오픈 로직을
`_openAggregationSelector()` 사설 메서드로 추출해 `_backgroundShape`에도 재사용한다.
`BaseGridCore.js`에서는 인라인 CSS 템플릿 문자열의 `:hover` 종속 규칙을 제거하고 기본값을
바꾼다.

**Tech Stack:** encke-grid(캔버스 기반 커스텀 그리드 렌더링 라이브러리, 컴파일된 JS로
`src/lib/encke-grid`에 직접 커밋되어 있으며 별도 `.ts` 소스나 유닛테스트 하네스가 없음).

## Global Constraints

- 스펙 범위: `GridColumnFooterCell`(일반 컬럼 푸터)만 수정. `GridGroupSummaryRowCell`(행 그룹
  요약 푸터)은 이번 변경에서 제외하고 기존 동작(메뉴 아이콘 클릭으로만 오픈) 그대로 유지한다.
- `.encke-grid-select-aggregate-widget-btn:hover #Icon_material-close { fill: #7F9DB8; }`
  규칙(버튼 자체의 순수 hover 색상 효과)은 그대로 유지한다 — 제거 대상 아님.
- `GridSelectAggregationWidget.js`의 펼침/접힘 토글 로직(`_expend`, `is-expended` 클래스)은
  변경하지 않는다.
- 이 저장소의 encke-grid 코드에는 유닛 테스트 하네스가 없으므로 새 유닛 테스트를 추가하지
  않는다. 각 태스크는 `npm run build:test`(타입/빌드 검증)와 수동 브라우저 확인으로
  검증한다.

---

## Task 1: 컬럼 집계 푸터 배경 클릭으로 드롭다운 열기

**Files:**
- Modify: `src/lib/encke-grid/components/grid/GridCell.js` (`GridColumnFooterCell` 클래스,
  대략 5052~5148줄 구간)

**Interfaces:**
- Consumes: 기존 `this._core.dispatchEvent`, `this.getAbsBoundary()`, `this.columnId`,
  `this._core.styleSheet.footer.iconDisabled`, `this._core.settings.footer.visibleTypeSelector`
  (모두 기존 코드에 이미 존재).
- Produces: `GridColumnFooterCell._openAggregationSelector()` — 인자 없음, 반환값 없음.
  가드를 통과하면 `footer-cell-click-end` 커스텀 이벤트를 dispatch한다 (detail:
  `{ columnId: string, rect: DOMRect, isFiredRowGroup: false }`). 이 이벤트 형태는
  `BaseGridCore.js`의 `footer-cell-click-end` 리스너(4180번째 줄 부근)가 그대로 소비하므로
  변경하지 않는다.

- [ ] **Step 1: 현재 동작 확인 (베이스라인)**

  `npm run dev`로 개발 서버를 띄우고, 임의의 숫자 컬럼 푸터에서 우측 하단 메뉴 아이콘을
  hover했다가 클릭해 집계 타입 드롭다운이 열리는지 확인한다. 이어서 같은 컬럼 푸터의
  메뉴 아이콘이 *아닌* 부분(예: 좌측 값 텍스트 영역)을 클릭했을 때 드롭다운이 열리지
  *않는* 현재 동작(버그 수정 전 상태)을 확인한다.

- [ ] **Step 2: `_openAggregationSelector()` 메서드 추출**

  `GridCell.js`의 `GridColumnFooterCell` 클래스에서 `_updateMenuIconVisible()` 메서드
  (현재 5144~5148줄 부근) 바로 다음에 아래 메서드를 추가한다.

  ```js
  _openAggregationSelector() {
      const isSelectedFrame = this._core.styleSheet.footer.iconDisabled !== true;
      const available = isSelectedFrame && this._core.settings.footer.visibleTypeSelector;
      if (!available) {
          return;
      }
      this._core.dispatchEvent(new CustomEvent('footer-cell-click-end', {
          detail: {
              columnId: this.columnId,
              rect: this.getAbsBoundary(),
              isFiredRowGroup: false,
          }
      }));
  }
  ```

  이 가드(`isSelectedFrame`, `available`)는 `_updateMenuIconVisible()`에서 쓰는 것과
  동일한 조건으로, 메뉴 아이콘이 비활성 상태일 때는 클릭으로도 드롭다운이 열리지
  않도록 맞춘 것이다.

- [ ] **Step 3: 기존 `_menuIcon` 클릭 리스너를 새 메서드 호출로 교체**

  생성자 안의 아래 블록을:

  ```js
          // 메뉴 아이콘 클릭 시에만 집계 타입 드롭다운 오픈
          this._menuIcon.addEventListener('click', () => {
              this._core.dispatchEvent(new CustomEvent('footer-cell-click-end', {
                  detail: {
                      columnId: this.columnId,
                      rect: this.getAbsBoundary(),
                      isFiredRowGroup: false,
                  }
              }));
          });
  ```

  아래로 교체한다:

  ```js
          // 메뉴 아이콘 클릭 시 집계 타입 드롭다운 오픈
          this._menuIcon.addEventListener('click', () => {
              this._openAggregationSelector();
          });
  ```

- [ ] **Step 4: `_backgroundShape`에 클릭 리스너 추가**

  같은 생성자 안, `this._backgroundShape.addEventListener('mouseout', ...)` 블록 바로
  다음(그리고 `this._menuIcon.addEventListener('mouseover', ...)` 이전)에 아래를 추가한다.

  ```js
          // 배경 영역 클릭 시에도 집계 타입 드롭다운 오픈
          this._backgroundShape.addEventListener('click', () => {
              this._openAggregationSelector();
          });
  ```

- [ ] **Step 5: 빌드 검증**

  Run: `npm run build:test`
  Expected: 에러 없이 빌드 성공.

- [ ] **Step 6: 수동 브라우저 검증**

  `npm run dev`로 개발 서버를 띄우고:
  - 일반 컬럼 푸터의 메뉴 아이콘 바깥쪽(배경) 영역을 클릭 → 집계 타입 드롭다운이 열리는지 확인.
  - 메뉴 아이콘을 직접 클릭해도 여전히 동일하게 열리는지 확인 (회귀 없음).
  - 드롭다운이 열린 상태에서 같은 푸터를 다시 클릭하면(300ms 이내) 토글 닫힘이 여전히
    동작하는지 확인 (`AggregationTypeSelector`의 기존 토글-닫기 로직, 변경 없음).
  - 행 그룹 요약 푸터(row grouping 사용 시 나오는 요약 행)에서는 배경 클릭으로 열리지
    *않고* 메뉴 아이콘 클릭으로만 열리는 기존 동작이 유지되는지 확인 (이번 변경은
    `GridColumnFooterCell`에만 적용되었으므로 회귀가 없어야 함).

- [ ] **Step 7: Commit**

  ```bash
  git add src/lib/encke-grid/components/grid/GridCell.js
  git commit -m "feat(grid): 집계 푸터 컬럼 클릭 시에도 집계 타입 드롭다운 오픈"
  ```

---

## Task 2: 선택 영역 집계 위젯 버튼 상시 노출

**Files:**
- Modify: `src/lib/encke-grid/components/grid/BaseGridCore.js` (인라인 CSS 템플릿,
  대략 342~371줄 구간)

**Interfaces:**
- Consumes: 없음 (순수 CSS 변경, `GridSelectAggregationWidget.js`의 `is-expended` 클래스
  토글 로직은 그대로 사용).
- Produces: 없음 (이 태스크의 결과를 다른 태스크가 참조하지 않음).

- [ ] **Step 1: 현재 동작 확인 (베이스라인)**

  `npm run dev`로 개발 서버를 띄우고, 그리드에서 셀 범위를 선택해 우측 하단에 집계 위젯이
  뜨는지 확인한다. 위젯 컨테이너를 hover하지 않은 상태에서는 펼침 버튼의 화살표 아이콘이
  보이지 않고 버튼 폭이 좁은(10px) 현재 동작을 확인한다.

- [ ] **Step 2: 버튼 기본 스타일 변경**

  `BaseGridCore.js`에서 아래 블록을:

  ```js
      .encke-grid-select-aggregate-widget-btn {
        background-color: #4073E9;
        border: 0;
        // border-radius: 2px;
        width: 10px;
        height: 100%;
        outline: none;
        padding: 0;
        background-repeat: no-repeat;
        background-position: center;
        // margin: 9px 2px 8px 8px;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      .encke-grid-select-aggregate-widget-btn svg {
        display: none;
      }
      .encke-grid-select-aggregate-widget:hover .encke-grid-select-aggregate-widget-btn {
        width: 18px;
      }
      .encke-grid-select-aggregate-widget-btn:hover #Icon_material-close {
        fill: #7F9DB8;
      }
      .encke-grid-select-aggregate-widget:hover .encke-grid-select-aggregate-widget-btn svg {
        display: block;
      }
      .encke-grid-select-aggregate-widget-btn.is-expended svg {
        transform: scaleX(-1);
      }
  ```

  아래로 교체한다:

  ```js
      .encke-grid-select-aggregate-widget-btn {
        background-color: #4073E9;
        border: 0;
        // border-radius: 2px;
        width: 18px;
        height: 100%;
        outline: none;
        padding: 0;
        background-repeat: no-repeat;
        background-position: center;
        // margin: 9px 2px 8px 8px;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      .encke-grid-select-aggregate-widget-btn svg {
        display: block;
      }
      .encke-grid-select-aggregate-widget-btn:hover #Icon_material-close {
        fill: #7F9DB8;
      }
      .encke-grid-select-aggregate-widget-btn.is-expended svg {
        transform: scaleX(-1);
      }
  ```

  (hover 전용이었던 `width: 18px`/`svg { display: block; }` 규칙을 제거하고 기본값에
  직접 반영했다. `#Icon_material-close` hover 색상 효과와 `is-expended` 뒤집기 효과는
  그대로 유지했다.)

- [ ] **Step 3: 빌드 검증**

  Run: `npm run build:test`
  Expected: 에러 없이 빌드 성공.

- [ ] **Step 4: 수동 브라우저 검증**

  `npm run dev`로 개발 서버를 띄우고, 셀 범위를 선택해 집계 위젯을 띄운 뒤:
  - 위젯을 hover하지 않아도 펼침 버튼의 화살표 아이콘이 처음부터 보이는지 확인.
  - 버튼 클릭 시 펼침/접힘 토글(`is-expended`)과 화살표 방향 반전이 정상 동작하는지 확인.
  - 버튼에 마우스를 올렸을 때 아이콘 색상이 여전히 바뀌는지(`#Icon_material-close` hover
    효과) 확인.

- [ ] **Step 5: Commit**

  ```bash
  git add src/lib/encke-grid/components/grid/BaseGridCore.js
  git commit -m "fix(grid): 집계 위젯 펼침 버튼을 hover 없이 항상 노출"
  ```

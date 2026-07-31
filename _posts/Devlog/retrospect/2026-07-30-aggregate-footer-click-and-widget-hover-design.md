# 집계 푸터 클릭 영역 확장 및 위젯 버튼 상시 노출

날짜: 2026-07-30
프로젝트: grid-service-web

## 배경

`encke-grid` 캔버스 그리드에는 두 개의 독립적인 UI 개선 요청이 있다.

1. 컬럼 집계 푸터(`GridColumnFooterCell`)에서 집계 타입 드롭다운(`AggregationTypeSelector`)을
   여는 방법이 현재는 우측 하단의 작은 `menuIcon`을 클릭하는 것뿐이다. 푸터 셀 영역 전체를
   클릭해도 동일하게 드롭다운이 열리도록 확장한다.
2. 선택 영역 집계 위젯(`GridSelectAggregationWidget`)의 펼침/접힘 토글 버튼
   (`.encke-grid-select-aggregate-widget-btn`)이 현재는 위젯 컨테이너를 hover해야만
   아이콘과 확장 너비가 보인다. hover 여부와 무관하게 항상 보이도록 변경한다.

## 범위

- 대상: `GridColumnFooterCell` (일반 컬럼 집계 푸터)만. 행 그룹 요약 푸터(`GridGroupSummaryRowCell`)는
  이번 변경에서 제외한다 (사용자 확인, 2026-07-30).
- 대상 파일:
  - `src/lib/encke-grid/components/grid/GridCell.js`
  - `src/lib/encke-grid/components/grid/BaseGridCore.js`

## 변경 1 — 집계 푸터 컬럼 클릭 시 드롭다운 오픈

`GridColumnFooterCell` 생성자(`GridCell.js`)에서 현재 `_menuIcon`의 `click` 리스너가
인라인으로 `footer-cell-click-end` 커스텀 이벤트를 dispatch한다.

- 이 로직을 `_openAggregationSelector()` 프라이빗 메서드로 추출한다.
  - 메서드 내부에서 `_updateMenuIconVisible()`이 쓰는 것과 동일한 가드
    (`isSelectedFrame = this._core.styleSheet.footer.iconDisabled !== true`,
    `available = isSelectedFrame && this._core.settings.footer.visibleTypeSelector`)를
    확인하여, 메뉴 아이콘이 비활성 상태일 때는 배경 클릭으로도 드롭다운이 열리지 않게 한다.
  - 가드를 통과하면 기존과 동일한 `footer-cell-click-end` 이벤트(detail: `columnId`, `rect`,
    `isFiredRowGroup: false`)를 dispatch한다.
- `_menuIcon`과 `_backgroundShape` 양쪽의 `click` 리스너가 이 메서드를 호출하도록 등록한다.
- `_backgroundShape`는 이미 `isEventTarget = true`로 hover 리스너만 등록되어 있어 click
  리스너 추가만으로 기존 hover/이벤트 흐름과 충돌하지 않는다. 동일 파일의
  `GridIndicatorFooterCell`이 배경 shape에 `click` 리스너를 붙이는 선례가 있다.

### 영향받지 않는 부분

- `AggregationTypeSelector`, `ColumnManager` 등 `footer-cell-click-end` 이벤트를 구독하는
  쪽은 이벤트 detail 형태가 그대로이므로 변경 없음.
- `GridGroupSummaryRowCell`(행 그룹 요약 푸터)은 이번 변경 범위 밖이며 기존 동작(메뉴 아이콘
  클릭으로만 오픈) 그대로 유지.

## 변경 2 — 위젯 버튼 상시 노출

`BaseGridCore.js`의 인라인 스타일 템플릿에서:

- `.encke-grid-select-aggregate-widget-btn`의 기본 `width`를 `10px` → `18px`로 변경하고,
  `.encke-grid-select-aggregate-widget:hover .encke-grid-select-aggregate-widget-btn { width: 18px; }`
  규칙은 제거한다(이미 기본값이 18px이므로 불필요).
- `.encke-grid-select-aggregate-widget-btn svg`의 기본 `display`를 `none` → `block`으로
  변경하고, `.encke-grid-select-aggregate-widget:hover .encke-grid-select-aggregate-widget-btn svg { display: block; }`
  규칙은 제거한다.
- `.encke-grid-select-aggregate-widget-btn:hover #Icon_material-close { fill: #7F9DB8; }`는
  버튼 자체의 순수 hover 색상 효과이므로 요청 범위 밖이며 그대로 유지한다.
- `GridSelectAggregationWidget.js`의 펼침/접힘 토글 로직(`_expend`, `is-expended` 클래스)은
  변경하지 않는다.

## 테스트

- 단위 테스트: `encke-grid`는 별도 소스 없이 컴파일된 JS로 관리되고 있어 기존 단위 테스트
  커버리지가 없다. 새 단위 테스트를 추가하지 않는다 (기존 컨벤션 유지).
- 수동 확인:
  - 그리드에서 일반 컬럼 푸터 영역(메뉴 아이콘 바깥쪽 포함) 클릭 시 집계 타입 드롭다운이 열리는지 확인.
  - 메뉴 아이콘 비활성 조건(`visibleTypeSelector: false` 등)에서 푸터 클릭 시 드롭다운이 열리지
    않는지 확인.
  - 행 그룹 요약 푸터는 기존과 동일하게 메뉴 아이콘 클릭으로만 열리는지 확인(회귀 없음).
  - 셀 범위 선택 후 나타나는 집계 위젯의 펼침 버튼이 위젯 hover 없이도 항상 보이는지 확인.
- 관련 Cypress 케이스가 있으면 로컬에서 실행 (커밋 전 CLAUDE.md 규칙에 따름).

## 미해결/후속 사항

- 행 그룹 요약 푸터(`GridGroupSummaryRowCell`)에도 동일한 클릭 확장을 적용할지는 이번 범위에서
  제외했으며, 필요 시 별도 요청으로 다룬다.

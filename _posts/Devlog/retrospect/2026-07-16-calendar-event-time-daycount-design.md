# Design: 캘린더 이벤트 시작시간 표기 및 멀티데이 "(전체 N일)" 표기

## 배경

`GraphCalendar`(월/주/일 뷰)에서 이벤트 표시 방식을 개선한다.

1. 월뷰 이벤트 title 앞에 시작시간을 표기한다.
2. 주뷰(및 일뷰) 종일줄에서 여러 날에 걸친 이벤트는 title 옆에 "(전체 N일)"을 표기한다.
3. 월뷰에서 종료시간이 있는(하루종일이 아닌) 이벤트가 여러 날에 걸쳐 "긴 바" 형태로 표시될 때, 디자인을 종일뷰 이벤트와 동일하게(호버 효과 제외) 바꾼다.

## 현재 구조 확인

- `GraphManagerBase.tsx`의 `generateEvents()`가 각 일정에 `allDay`, `start_time`, `end_time`, `start_date`, `end_date` 등을 계산해 `this.tasks`에 담고, `GraphCalendar.tsx`가 이를 그대로 FullCalendar `events` prop에 넘긴다. `title/start/end/allDay` 외 필드는 FullCalendar가 자동으로 `event.extendedProps`에 담는다.
- 이벤트 콘텐츠 렌더링은 `GraphCalendar.tsx`의 `CustomEventContent()` 한 곳에서 처리한다.
  - `timeGridWeek`/`timeGridDay`에서 `!allDay`(시간 있는 이벤트)인 경우: 전용 분기(`calendar-timegrid-event-*`, 3003~3027번 줄)를 탄다.
  - 그 외 모든 경우(월뷰 전체 + 주/일뷰 종일줄): 공용 fallback 분기(3029~3033번 줄, `fc-event-title`만 렌더링)를 탄다.
  - 즉 fallback 분기에서 `!event.allDay`이면 항상 "월뷰(단일일자 또는 멀티데이 바)"이고, `event.allDay`이면 항상 "주/일뷰의 종일줄 또는 월뷰의 all-day 이벤트"다. 뷰 타입을 별도로 검사하지 않아도 `allDay` 플래그만으로 대상이 정확히 갈린다.
- 주/일뷰 종일줄 이벤트는 이미 전용 CSS(가운데정렬, 스트라이프 없음, 둥근모서리, inset box-shadow, `:hover` 시 배경색 변경)를 갖고 있다(`GraphCalendar.scss` 1460~1548번 줄, 1911~1923번 줄 부근에 각 뷰별로 중복 존재). 월뷰 이벤트는 좌측 스트라이프가 있는 별도 스타일 하나만 존재하며, all-day/timed/단일/멀티 구분 없이 전부 동일한 스타일을 공유한다.
- `GraphManagerBase.tsx`의 `isCalendarAllDayEvent()`는 시작시각이 자정이 아니면 무조건 `false`(=시간 있는 이벤트)를 반환한다. 따라서 `allDay=false`인 이벤트는 항상 "실제로 의미 있는 시작시각"을 가진다(우연히 00:00:00인 극단적 케이스 포함 — 이 경우도 `allDay=false`이면 시간 표기 규칙을 그대로 적용한다).

## 결정된 규칙

### 1) 월뷰 시작시간 표기
- `CustomEventContent`의 fallback 분기에서 `!event.allDay`일 때, `event.extendedProps.start_time`("HH:mm:ss.SSS")을 앞 5글자(`HH:mm`)만 잘라 title 앞에 붙인다.
- 규칙은 `allDay` 플래그 기준으로만 판단한다(개별 시각 문자열이 우연히 "00:00"이어도 `allDay=false`면 표기).
- 단일일자 이벤트와 멀티데이 바 이벤트에 동일하게 적용된다(별도 분기 불필요).

### 2) "(전체 N일)" 표기
- 같은 fallback 분기에서, FullCalendar가 넘겨주는 `event.start`/`event.end`(end는 exclusive)로 `totalDays = Math.round((end - start) / 86400000)`를 계산한다.
- `totalDays > 1`이면 title 뒤에 ` (전체 ${totalDays}일)`을 이어붙인다. title과 동일한 엘리먼트/스타일을 그대로 사용하므로(문자열만 이어붙임) 별도 CSS가 필요 없다.
- 적용 대상: 주뷰 종일줄(원 요청) + 일뷰 종일줄 + 월뷰의 기존 all-day 멀티데이 바 + 월뷰의 새로 디자인 변경되는 timed 멀티데이 바(3번 항목). 즉 "여러 날에 걸치는 모든 이벤트"에 일관되게 적용한다. 월뷰 all-day 바의 기존 디자인(좌측 스트라이프)은 변경하지 않고 텍스트만 추가된다.

### 3) 월뷰 timed 멀티데이 바 디자인 변경
- 적용 대상은 `view.type === 'dayGridMonth' && !event.allDay && totalDays > 1`인 이벤트만이다. 기존 all-day 멀티데이 바(month view)는 지금의 좌측 스트라이프 디자인을 그대로 유지한다.
- `eventClassNames` 콜백에 위 조건을 추가해 새 클래스(`is-month-timed-multiday`)를 부여한다.
- `GraphCalendar.scss`에 해당 클래스 전용 규칙을 추가한다. 주/일뷰 종일줄 스타일(가운데정렬, 스트라이프 없음(`.fc-event-bar-stripe { display: none }`), 둥근모서리, inset box-shadow)을 그대로 재사용하되, `:hover` 시 배경색/box-shadow가 바뀌는 규칙은 포함하지 않는다("hover 기능 제외" 요구사항).
- 시간 표기(1번)와 "(전체 N일)" 표기(2번)는 별도 구현 없이 동일 fallback 분기 로직이 그대로 적용된다.

## 영향 파일 (Blast radius)

- `src/components/graph/calendar/GraphCalendar.tsx`
  - `CustomEventContent()`: fallback 분기 로직 추가(시간 prefix, 일수 suffix)
  - `eventClassNames` 콜백: `is-month-timed-multiday` 클래스 추가
- `src/components/graph/calendar/GraphCalendar.scss`
  - 새 클래스용 규칙 추가(주/일뷰 종일줄 스타일 재사용, hover 제외)
  - 주의: `.list-view-body-row.is-today` 블록은 사용자가 수동 관리 중이므로 건드리지 않는다.
- `src/components/graph/GraphManagerBase.tsx`: 수정 불필요(데이터는 이미 충분함)

## Non-goals

- `custom`(리스트/agenda) 뷰의 표기 방식(`CalendarListViewRows.ts`의 `(dayIndex/totalDays일)` 포맷)은 이번 변경 대상이 아니다. 별개 뷰, 별개 포맷이며 그대로 둔다.
- 이벤트 드래그/리사이즈 등 상호작용 로직은 변경하지 않는다(디자인만 변경, "hover 기능 제외"는 시각 효과 제거를 의미하며 드래그/리사이즈 가능 여부 자체는 건드리지 않는다).
- `isCalendarAllDayEvent()` 등 이벤트 데이터 생성 로직은 변경하지 않는다.

## 테스트 시나리오

1. 월뷰 단일일자 이벤트(시작 09:00): title 앞에 "09:00 " 표기.
2. 월뷰 단일일자 종일 이벤트(allDay=true): 시간 표기 없음(기존과 동일).
3. 월뷰 멀티데이 all-day 바(예: 3일): 좌측 스트라이프 디자인 유지, title 뒤에 "(전체 3일)" 추가.
4. 월뷰 멀티데이 timed 바(시작 09:00, 여러 날): 종일뷰와 동일한 가운데정렬/스트라이프없음 디자인 + 호버 효과 없음 + "09:00 " 접두 + "(전체 N일)" 접미.
5. 주뷰 종일줄, 여러 날짜에 걸친 이벤트: title 뒤에 "(전체 N일)" 표기, 디자인은 기존 그대로.
6. 주뷰 종일줄, 단일일자 이벤트: 일수 표기 없음(기존과 동일).
7. 일뷰 종일줄, 여러 날짜에 걸친 이벤트: 5번과 동일하게 "(전체 N일)" 표기.
8. 주/일뷰의 시간 있는(timed, 종일줄 아님) 이벤트: 이번 변경으로 영향받지 않음(기존 `calendar-timegrid-event-*` 분기 그대로).

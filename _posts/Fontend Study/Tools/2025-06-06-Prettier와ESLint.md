---
title: "[Tools] 커밋하신 코드가 다 틀어졌는데요? – Prettier와 ESLint가 필요한 이유"
toc: true  
toc_label: "목차"  
toc_sticky: true  
category: "environment"
---

## 🚀 시작하며

최근 프로젝트에서 프론트엔드 이슈를 수정해보라는 미션을 받았습니다.
 기존 코드에서 발생한 문제를 직접 분석하고 고치는 과정이었고,
 수정 자체는 무난하게 마무리한 뒤 커밋까지 완료했죠.

그런데…

커밋 후, 선배님께서 다가오시더니 이렇게 말씀하셨습니다.

> “혹시 ESLint 설정 안 돼 있나요? 지금 코드 전부 틀어졌는데요?”

깜짝 놀라 확인해보니,
 **터미널에는 ESLint warning이 화면 가득 쏟아지고 있었습니다.**
 스타일이 엉망이었고, 뭔가 이상했죠.
 하지만 제 로컬에는 분명히 ESLint 설정이 정상적으로 되어 있었거든요.

이유를 찾아보던 선배님께서 설명해주셨습니다.
 **ESLint 설정이 주석 처리된 상태였고, 그 상태로 커밋이 이뤄졌던 것**이었습니다.
 같이 작업하시던 다른 리더님께서 임시로 설정을 꺼두셨던 건데,
 그게 다시 활성화되지 않은 채로 제 작업에 영향을 준 거죠.

그 상황에서 또 다른 리더님이 오셔서,
 "나중에 같이 다시 보자"며 상황을 정리해주셨고,
 전 함께하는 프로젝트에서의 규칙의 중요성을 깨달았습니다.

> “Prettier랑 ESLint가 없으면, 이렇게 작은 코드 하나도 수십 개의 문제를 만들 수 있구나.”
>  “도대체 이 도구들은 왜 존재하고, 왜 이렇게 중요하게 여겨지는 걸까?”

이 글에서는 그 질문에 대한 답을 찾아가기 위해,
 **Prettier와 ESLint의 정의, 탄생 배경, 실제 역할, 함께 사용할 때의 시너지와 이점까지** 정리해보려고 합니다.!

------

## 코드 스타일 도구란?

> 코드 스타일 도구란, **개발자가 작성한 코드의 형식이나 문법 규칙을 자동으로 정리하거나 검사해주는 도구**입니다.

이런 도구들은 코드의 가독성과 일관성을 유지하여 코드 품질을 유지하고 협업에서 충돌을 줄이기 위해 쓰입니다.

### 왜 필요한가?

개발자마다 코딩 스타일은 다 다릅니다. 그래서 그 스타일의 사소한 차이들이 쌓이면 협업시에 불필요한 시간 낭비가 생기기때문에 이 스타일을 통일시켜주는 자동화 도구로 코드 스타일 도구가 필요합니다.

## Prettier란?

> **Prettier**는 코드 포메터<small>(Formatter)</small>입니다. 즉, **코드 스타일을 자동으로 맞춰주는 도구**입니다.

### 만들어진 이유

Prettier의 홈페이지에서는 Prettier를 도입한 가장 큰 이유로 스타일 논쟁을 종식하기 위함이라고 말합니다.

프로젝트와 팀에 공통된 스타일 가이드를 갖는 것이 중요하다는 것은 보편적으로 알려져 있지만, 그 과정이 매우 복잡하기 때문에 Prettier를 통해 이 문제를 해결하는 겁니다. 

- 개발자마다 선호하는 코드 스타일이 달라 충돌발생
- 협업 시 스타일 논쟁은 시간 낭비!

 ➡️ Prettier 탄생



### 역할

Prettier는 다음과 같은 역할을 합니다.

- 들여쓰기, 괄호, 세미콜론 위치 등 형식적인 코드 스타일을 통일
- 설정한 규칙에 따라 코드를 자동으로 정렬 및 재구성

❗ 문법 오류를 잡지는 않습니다. 오직 스타일만 ❗



**예시**

``` javascript
// Prettier 적용 전
function hello( ) {console.log("hi")}

// Prettier 적용 후
function hello() {
  console.log("hi");
}
```

### Prettier의 동작 원리

그렇다면 Prettier는 어떻게 내 코드 스타일을 통일 하는 것일까?

1. 코드를 파싱한다.

   Prettier는 코드를 **AST<small>(Abstract Syntax Tree)</small>**로 바꿔서 내부 구조를 이해합니다.

   > **AST<small>(Abstract Syntax Tree)</small>**란?
   >
   > 프로그래밍 언어의 코드를 트리 구조로 표현한 것입니다.
   >
   > 예를 들면
   >
   > ``` javascript
   > const a = 3 + 5;
   > ```
   >
   > 이 자바스크립트 코드를 AST로 바꾼다면
   >
   > ``` javascript
   > VariableDeclaration
   > ├── Identifier (a)
   > └── BinaryExpression (+)
   >     ├── Literal (3)
   >     └── Literal (5)
   > ```
   >
   > 이렇게 됩니다.
   >
   > AST는 컴파일러, 번들러, 린터, 트랜스파일러 같은 애들이 사용하는 핵심 재료로 위와 같은 코드 처리 도구들이 AST를 분석해서 코드 구조를 이해한 뒤에 뭔가 수정하는 것입니다.

2. 스타일 규칙에 따라 재작성한다.

   AST를 기반으로 정해진 포맷팅 규칙에 따라 새롭게 포맷팅된 코드를 생성합니다. 예를들어 세미콜론, 따옴표, 줄 길이, 공백 등이 여기에 포함됩니다.

3. 기존 코드를 통째로 교체한다.

   기존 코드를 통째로 덮어쓰면서 스타일을 강제 통일합니다.

   무조건 정해진 방식대로 밀어붙이기 때문에 향간에서 Prettier는 의견이 없다.(opinionated)는 말도 듣는다고 합니다. 

## ESLint란?

> **ESLint**는 "정적 분석 기반의 린팅 도구(Linter)"입니다. 즉, **문법 오류나 코드 품질 문제를 사전에 검출하는 도구**입니다.

### 만들어진 이유

자바스크립트는 유연한 언어이기 때문에 **실수로도 돌아가는 코드**가 많습니다. 그러나 이런 그 코드는 종종 버그를 유발합니다. 그래서 ESLint를 사용하여 코드 품질 문제를 해결하는 것입니다.

### 역할

- 오타, 미사용 변수, 잘못된 패턴 등을 잡음
- 팀 컨벤션에 맞지 않는 코드도 경고
- 플러그인/설정에 따라 React, TypeScript 등 다양한 환경 대응 가능



**예시**

``` javascript
let a = 1;
console.log(b); // 'b is not defined' ESLint 경고
```

###  ESLint의 동작 원리

앞에서 Prettier를 설명했을 때와 같이 ESLint도 AST를 이해한뒤 동작합니다.

1. 코드를 파싱한다.

   ESLint도 코드를 AST로 파싱해서 구조를 이해합니다.

2. 정의된 룰 목록과 비교한다.

   `.eslintrc`에 설정된 규칙들과 코드를 비교하면서 규칙 위반 여부를 탐색합니다.

3. 위반 시 경고 또는 오류를 표시한다.

   터미널이나 IDE에서 경고를 표시합니다.

   일부 규칙은 `--fix` 옵션으로 자동 수정이 가능합니다.

## Prettier와 ESLint의 차이

| 항목      | Prettier                         | ESLint                                 |
| --------- | -------------------------------- | -------------------------------------- |
| 목적      | 코드 스타일 통일                 | 코드 오류 검출, 코드 품질 향상         |
| 포커스    | 들여쓰기, 괄호, 세미콜론 등 포맷 | 변수 사용, 문법 오류, 안티패턴 등 검출 |
| 역할      | 포맷터(Formatter)                | 린터(Linter)                           |
| 자동 수정 | O                                | O (일부만)                             |

➡️ **Prettier는 보기 좋게 정리하고**, **ESLint는 논리적 문제를 잡는다**

## 함께 쓸 때의 시너지

Prettier와 ESLint는 서로 보완적인 역할을 하므로 **같이 쓰는 것이 거의 표준**입니다.

### ✅ 함께 쓸 때 장점

- 스타일과 문법 오류 모두 자동화
- 개발자가 아닌 툴이 판단하므로 **코드 리뷰에서 스타일 논쟁이 줄어듦**
- 일관된 코드 → 유지보수 용이

### ✅ 추천 조합

ESLint + Prettier + `eslint-config-prettier` + `eslint-plugin-prettier` 

➡️ 충돌 방지 + 통합 적용 가능



## 실제로 겪은 경험에서 배운 점

이번 경험을 통해, 프로젝트에 설정된 ESLint가 정상적으로 작동하지 않는 상황이 **얼마나 쉽게 실수를 유발할 수 있는지** 체감하게 됐습니다.

Prettier는 적용되어 코드가 깔끔하게 정리되었지만, ESLint가 비활성화된 상태였기 때문에 **문법적 경고나 규칙 위반이 커밋되기 전까지 전혀 보이지 않았던 것**이죠.

결과적으로 저는 다음과 같은 교훈을 얻었습니다:

- **모든 팀원이 동일한 설정을 유지하도록 주기적으로 체크해야 한다.**
- VSCode에서 `.eslintrc`, `.prettierrc` 설정이 제대로 인식되고 있는지도 항상 확인해야 한다.
- `husky`, `lint-staged` 같은 도구를 활용해 **커밋 전에 자동으로 체크되게 해야 한다.**
- 그리고 **무엇보다 커밋 전 warning이 떴다면 반드시 꼼꼼히 확인하고 원인을 파악했어야 했다.**

그 작은 경고 하나를 넘기지 않았다면, 불필요한 리뷰 지적도 줄이고, 팀의 설정 문제도 더 빨리 파악할 수 있었을 것입니다.
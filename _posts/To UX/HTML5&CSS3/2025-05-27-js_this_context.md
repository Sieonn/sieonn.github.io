---
title: "[To UX] this는 누구를 가리키고 있을까?"
toc: true
toc_label: "목차"
toc_sticky: true
category: "JavaScript"
---

## 🚀 시작하며

`JavaScript`로 코드를 작성하거나 작성된 코드를 뜯어볼 때, `this`가 그래서 어떤 것을 가리키는 걸까? 하면서 헷깔릴때가 있습니다.

오늘 글을 작성하면서 `this`와 실행 컨텍스트의 개념을 정리하면서 이를 통해서 실행 원리를 시각화하고 프론트엔드 컴포넌트 설계에서 발생할 수 있는 혼란을 줄이려고 합니다. 

------

## 실행 컨텍스트 (Execution Context)

### ✅ 정의

> **코드가 실행되는 환경(context)**을 의미하며, `JavaScript` 엔진이 코드를 해석하고 실행하기 위해 생성하는 객체

`JavaScript`는 코드를 실행할 때 **실행 컨텍스트 스택(Call Stack)**을 만들어 관리합니다.

스택이니까 **후입선출(LIFO)** 방식입니다.

함수가 나중에 호출되면 먼저 끝나고 먼저 호출된 함수는 나중에 끝난다는 이야기 입니다.



#### 실행 컨텍스트 스택 작동 원리

1. 코드 실행이 시작되면 `Global Execution Context(전역 실행 컨텍스트)`가 제일 먼저 스택에 올라갑니다.
2. 함수를 호출하면 그 함수의 Execution Context가 위에 추가(push)됩니다.
3. 함수 실행이 끝나면 해당 컨텍스트는 스택에서 제거(pop)됩니다.

``` javascript
function first() {
  console.log("첫 번째");
  second();
}

function second() {
  console.log("두 번째");
}

first();
```

이것을 예로 봤을때는 

`first()`호출이 되고 함수 내부의 `console.log("첫 번째")`를 출력하지만 `second()`가 호출되면서 나중에 호출된 `second()`함수부터 실행됩니다.
`second()`함수가 끝나면 `first()`함수가 끝납니다.

그래서 후입선출 같아보입니다.

출력이라는 것 때문에 return이나 console.log()면 pop인거 아닌가 했는데 함수의 끝을 이야기하는 겁니다.

> 호출되면 **push**, 끝나면 **pop**

```js
function outer() {
  let a = 1;
  function inner() {
    console.log(a);
  }
  inner();
}
outer();
```

### 🔍 내부 구성 요소

- **Variable Environment**: 변수, 함수 선언 정보
- **Lexical Environment**: 현재 스코프, 클로저 정보
- **`this` 바인딩**: 상황에 따라 결정됨

### 🧠 실행 순서

1. Global Context 생성 → `this`는 window(global)
2. 함수 호출 → 새로운 Context 생성
3. Context 스택에서 가장 위에 있는 게 현재 실행 중인 컨텍스트

------

## this 바인딩 (This Binding)

### ✅ 정의

> **현재 실행 중인 컨텍스트에서 사용되는 객체를 가리키는 키워드**

`JavaScript`에서 `this`는 선언 위치가 아닌 **호출 방식에 따라** 달라집니다.

### 📌 5가지 this 바인딩 규칙

#### 1) 전역 컨텍스트

```js
console.log(this); // 👉 window (브라우저 기준)
```

#### 2) 함수 호출 (일반)

```js
function sayHi() {
  console.log(this);
}
sayHi(); // 👉 window (strict 모드에선 undefined)
```

#### 3) 객체 메서드 호출

```js
const person = {
  name: "시언",
  greet() {
    console.log(this.name);
  }
};
person.greet(); // 👉 "시언"
```

#### 4) 생성자 함수 (new)

```js
function User(name) {
  this.name = name;
}
const user = new User("시언");
console.log(user.name); // 👉 "시언"
```

#### 5) 명시적 바인딩 (call, apply, bind)

```js
function sayHello() {
  console.log(this.name);
}
const user = { name: "시언" };
sayHello.call(user); // 👉 "시언"
```

### 🧠 Arrow Function에서 this는?

> `this`는 **자신의 상위 스코프에서 결정됨 (Lexical this)**

```js
const obj = {
  name: "시언",
  greet: () => {
    console.log(this.name); // ❌ window.name (undefined)
  }
};
```

→ arrow function은 자신을 포함하는 외부 컨텍스트의 `this`를 그대로 사용함.

#### 왜 `this.name`이 undefined가 될까?

화살표 함수(`=>`)는 자신만의 `this`를 만들지 않습니다. 대신에 자신이 정의된 위치의 외부 스코프를 **정의된 위치(코드를 '쓴 장소')에 따라 this가 정해집니다.**



여기서 `greet: () => {}`는 `obj`라는 객체의 내부에서 실행되는게 아니라 전역 컨텍스트에서 정의된 함수입니다.
그래서 `this`는 전역객체(브라우저의`window`, `global` in Node.js)를 가리킵니다.

그래서 `window.name`이 없으면 undefined입니다.

> 👉 **`obj.greet()`처럼 객체로 호출해도, 화살표 함수는 무시하고 위쪽 스코프(this)를 본다.**
>
>
> 왜냐하면 객체 화살표 함수를 호출하더라도, 그 객체는 this 바인딩에 영향을 주지 못합니다. 왜냐하면 화살표 함수는 실행 컨텍스트를 기준으로 this를 바인딩하지 않기 때문입니다.

#### ✅ 일반 함수 vs 화살표 함수 — this 바인딩 시점

| 구분             | 일반 함수                       | 화살표 함수                         |
| ---------------- | ------------------------------- | ----------------------------------- |
| this 바인딩 시점 | **실행 시점** (누가 호출했느냐) | **정의 시점** (어디에서 정의됐느냐) |
| this 결정 기준   | **호출한 주체**                 | **외부 렉시컬 스코프**              |

#### 🧠 그럼 obj.greet() 호출인데 왜 obj가 this가 아닌가?

```javascript
const obj = {
  name: "시언",
  greet: () => {
    console.log(this.name);
  }
};

obj.greet();
```

#### 🔍 여기에 숨어 있는 구조

`greet: () => {}` ← **화살표 함수가 정의되는 순간**, 자바스크립트는 `this`를 "캡처"합니다.

greet이 정의되는 시점은 **obj 객체가 만들어질 때**, 그리고 이건 **전역 스코프에서 실행됩니다.**

> 그러니까 greet 내부의 `this`는 이미 정의 시점에 **window (또는 undefined, strict mode)** 로 고정된 상태입니다.

그 이후에 `obj.greet()`처럼 **객체로 호출하든, 배열에서 호출하든, 상관없이**`this`는 바뀌지 않습니다.

------

#### 📦 실행 컨텍스트가 생성되어도 `this`는 바뀌지 않는 이유?

보통 일반 함수는 실행 컨텍스트를 만들 때 다음 과 같은 작업을 합니다.

- VariableEnvironment
- LexicalEnvironment
- `this` 바인딩 ⬅️ 💥 여기서 **"누가 호출했는가"**를 기준으로 바인딩

그런데 **화살표 함수는 자체 실행 컨텍스트에 `this`를 바인딩하지 않습니다.**
 그 대신, **자기가 만들어질 당시의 외부 환경(상위 컨텍스트)의 this를 복사해서 씁니다.**

> 즉, 화살표 함수는 실행될 때 this를 "무시하고", 아예 **자기 스코프 바깥에서 미리 정해놓은 this**만 사용합니다.

------

## 🔍 정리

| 호출 방식     | this 값                       |
| ------------- | ----------------------------- |
| 전역          | window (브라우저)             |
| 함수          | window or undefined (strict)  |
| 메서드        | 해당 객체                     |
| 생성자        | 새로 생성된 객체              |
| 명시적 바인딩 | 지정한 객체 (call/apply/bind) |
| 화살표 함수   | 상위 스코프 this              |


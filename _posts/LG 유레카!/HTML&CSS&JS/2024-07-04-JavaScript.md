---
title: "[LG유레카] 2. JavaScript"
toc: true
toc_sticky: true
toc_label: true
---

## JavaScript

### 자바스크립트 특징

- 웹 개발을 위한 프로그래밍 언어

- 스크립트 언어

- 이벤트 드리븐 방식<small>(Event-Driven)</small>

  동파서, 삭스 파서중에서 삭스파서가 이벤트 드리븐

- 자바스크릡트 표준, ECMAScript

### 스크립트 언어

- 스크립트 언어란?

  - 프로그램 실행 시에 기계어로 변환(interpreted) ➡️ 통역

  - 편리하여 초보자도 익히기 쉬움

  - 자바스크립트, 파이선(python)

  - 컴파일<small>(compiled)</small>언어: 실행 이전에 변환 ➡️ 번역

    <img src="/../../images/2024-07-04-JavaScript/image-20240704142740709.png" alt="image-20240704142740709" style="zoom:80%;" />

### 이벤트 드리븐 방식

- 이벤트 드리븐 방식

  이벤트에 반응하여 동작을 변경하거나 며역을 수행하는 방식

  - 이벤트 : 대상+트리거(trigger)+처리기(handler/listener)

### 자바스크립트 연결하기

- HTML 이벤트 속성을 이용한 연결(높은 복잡도)

  ``` html
  <div id="box" onclick="document.getElementById('box').style.backgroundColor='magenta'">
  </div>
  ```

- \<script>\</script> 요소에서의 연결(추천 방법)

  ``` html
  <script>
      document.getElementById('circle').onclick=function(){
          document.getElementById('circle').style.backgroundColor ='green';
      }
      document.getElementById('circle').onclick=function(){
          this.style.backgroundColor = 'green';
          console.log(this);
      }
  </script>
  ```

  

>``` javascript
>function hello(){   
>}
>```
>
>➡️ 자바스크립트 함수는 일급객체
>
>➡️자바스크립트 함수는 클래스와 어깨를 나란히한다. 
>
>**❓일급객체의 특성이 무엇일까??**
>
>변수에 담을  수 있다.
>
>매개변수와 리턴 값으로 사용가능

### 콘솔 활용하기

- 브라우저의 디버깅 콘솔(console)

  - 자바스크립트의 오류나 비정산적인 연산의 원인 탐지 도구

    ![image-20240704144733284](/../../images/2024-07-04-JavaScript/image-20240704144733284.png)



### 명령형 프로그래밍과 선언형 프로그래밍

- 프로그래밍 패러다임

  - 명령형<small>(imperative)</small>

    명령어의 순차적 나열 - How 관점

  - 선언형<small>(declarative)</small>

    실행할 프로그램 선언 -  What관점➡️ 목표가 무엇인지

  - 자바스크립트는 명령형에 가깝지만, 두 가지 스타일 모두 지원

    ![image-20240704144952718](/../../images/2024-07-04-JavaScript/image-20240704144952718.png)

> **let**
>
> - 중복 선언 불가능
> - ECMAS6 부터 선언된 블럭에서만 사용할 수 있는 블록 변수(let)이 제공됨
> - 호이스팅 대상에서 제외
>
> **const**
>
> - 상수로 사용
> - 선언 시 값을 할당해야 함
> - 호이스팅 대상에서 제외
> - let 키워드와 값을 변결할 수 없다는 것만 제외하고 동일
>
> ✔️호이스팅은 인터프리터가 코드를 실행하기 전에 함수, 변수, 클래스 또는 임포트(import)의 선언문을 해당 범위의 맨 위로 끌어올리는 것 처럼 보이는 현상입니다.

### 함수와 메서드

- 함수<small>(function)</small>

  어떤 기능 수행을 위해 디자인된 명령어 모음

- 메서드<small>(method)</small>

  메서드 특정 객체와 연관된 명령어 모음

  <img src="/../../images/2024-07-04-JavaScript/image-20240704153649362.png" alt="image-20240704153649362" style="zoom:80%;" />
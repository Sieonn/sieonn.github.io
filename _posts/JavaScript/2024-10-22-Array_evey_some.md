---
title: "[JavaScript] Array every(), some()"
toc: true
toc_label: "목차"
toc_sticky: true
---

# 배열 처리

`every`와 `some`둘 다 특정 조건을 만족하는지 배열 내부의 원소를 순회하면서 검사합니다.

검사하면서 조건에 만족하면 True
만족하지 않으면 False를 리턴합니다.

➡ 배열의 원소 값에 대해서 검사가 필요할 때 사용



## Every()

조건을 만족하지 않으면 발견 즉시 순회를 멈춥니다.

``` javascript
let = [{name: 'eon', age: 28},
       {name: 'ing', age: 29},
      {name: 'hong', age:10}]

let result = data.evey(person => {
    return person.age >= 25
});

console.log(result);


============================================
   >> false
```

내부 원소가 모두 조건을 만족해야지 True를 출력합니다.

## Some()

조건을 만족하면 발견 즉시 순회를 멈춥니다.

``` javascript
let = [{name: 'eon', age: 28},
       {name: 'ing', age: 29},
      {name: 'hong', age:10}]
let result = data.some(person => {
    person.age<20});

console.log(result);

===============================================================
    >> True
```

배열 내부의 원소중에 하나라도 조건을 만족하면 True를 출력합니다.

<img src="/../images/2024-10-22-Array_evey_some/image-20241022014424719.png" alt="image-20241022014424719" style="zoom:80%;" />

우테코에서 some을 사용했던 부분이 있었습니다.

if문에서 배열 처리 some을 사용해서 저 조건이 만족하는 것이 하나라도 있으면 바로 error처리가 되도록 했습니다.


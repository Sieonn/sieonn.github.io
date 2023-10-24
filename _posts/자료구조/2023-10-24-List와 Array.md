---
title: "[자료구조] List, Array"
toc: "true"
toc_label: "List, Array"
toc_sticky: true
---

## List와 Array

### List(리스트)

리스트는 파이썬에서 가장 자주 사용되는 데이터 구조 중 하나입니다. 
여러 가지 다른 유형의 항목을 저장할 수 있는 유연성이 있습니다. 

생성하는 방법은 <span class="hlm">대괄호[ ]</span>를 사용하며, 각 요소는 쉼표로 구분합니다.

```python
new_list = [3, "Hi", 6.7]
num_list = [0, 1, 2, 3, 4]

array = int[5]
print(new_list)
```

{: .notice}

결과:<br/>TypeError: 'type' object is not subscriptable<br/>이는 자료형과 관련된 에러입니다. 리스트는 int를 통해 숫자형으로 변경 할 수 없습니다.<br>

### Array(배열)

배열은 <span class="hlm">동일한 유형의 값을 저장</span>할 수 있는 구조입니다. 리스트와 달리,  **배열의 모든 요소는 동일한 데이터 유형**이여야 한다. 배열은 `array`모듈을 사용하여 생성할 수 있으며, 별도로 import해야 합니다.

```python
import array as arr

my_array = arr.array('i', [1, 2, 3])
print(my_array)
```

{: .notice}

배열은 같은 데이터 유형으로 구성되어 있다. 에러가 발생한다.<br>

### List와 Array의 비교

| List                                                         | Array                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| - 대괄호`[ ]`로 쉽게 생성 가능<br >- 다양한 데이터 유형의 요소 저장 가능<br >- 쉬운 원소 추가를 위해 큰 메모리 필요<br >- 변경이 쉬움<br >- 직접적인 연산 불가능<br >- <span class="hlm">리스트 안에 리스트 중첩 가능</span><br >- 순서가 지정된 콜렉션 | - 선언 되어야 함<br >- <span class="hlm">array module이나 numpy 이용</span><br >- 적은 메모리 사용<br >- 한 요소에 대해 변경이 어려움<br >- 사칙 연산 쉬움<br >- 모든 요소가 <span class="hlm">같은 자료형</span><br >- 순서가 지정된 콜렉션 |

<br>

## List의 기본 동작

###  리스트의 생성과 초기화 방법

리스트를 생성하려면 대괄호`[]`를 사용하고, 각 요소를 쉼표 `,`로 구분합니다.

`empty_list = [] ` ◀ 빈 리스트 생성

<br>

### 리스트의 요소 접근 방법과 수정

요소에 접근하기 위해서는 <span class="hlm">인덱스</span>를 사용합니다. 이 인덱스는 0부터 시작합니다. 요소를 변경할 때, 이 인덱스를 사용해서 특정 위치의 요소를 변경할 수 있습니다.

```python
num_list = [1, 2, 3, 4, 5]

print(num_list[2])
# 출력: 3
```

<br>

### 리스트의 크기 조정(추가, 삭제)

리스트에 요소를 추가하려면 <span class="hlm">append()</span> 메서드를 사용합니다.

리스트에 요소를 삭제하려면 <span class="hlm">remove()</span>메서드를 사용합니다.

{: .notice--info}

**remove() 메소드**는 리스트에 중복된 값이 있을 경우에 첫 번째 값을 삭제합니다.

```python
num_list = [1, 2, 3, 4, 5]
num_list.append(6)
print(num_list)
#출력: [1, 2, 3, 4, 5, 6]

num_list = [1, 2, 3, 4, 5, 6]
num_list.remove(6)
print(num_list)
#출력: [1, 2, 3, 4, 5]
```

리스트에서 특정 위치의 요소를 삭제하려면 `del`키워드 또는 `pop()`메서드를 사용할 수 있습니다. **pop()메서드**는 <span class="hlm_h">삭제된 요소를 반환</span>하기 때문에 필요에 따라 사용할 수 있습니다.

```python
num_list = [1, 2, 3, 4, 5, 40]
del num_list[5]	# 인덱스 5의 요소 삭제
print(num_list)
#출력: [1, 2, 3, 4, 5]

num_list = [1, 2, 3, 4, 5]
pop_element = num_list.pop(2) #인덱스의 2의 요소 삭제 및 반환
print(pop_element) 
#출력: 3
```

<br>

## List의 다양한 활용

### 리스트를 활용한 반복문

파이썬의 리스트는 반복문에서 자주 사용됩니다. **for문**을 이용하여 리스트의 요소에 접근할 수 있습니다.

```python
num_list = [1, 2, 3, 4]

for i in num_list:
    print(i)
```

또한, 리스트 컴프리헨션(list comprehension)을 이용하여 리스트를 더욱 간결하게 생성하거나 변경할 수 있습니다.
`comprehension은 포괄과 이해라는 뜻으로 정의할 수 있습니다.`

{: .notice}

파이썬에서는 대괄호`[]`안에 **조건문과 반복문을 사용해서 표현된 식**으로 리스트를 초기화 할 수 있습니다.

```python
num_list = [1, 2, 3, 4, 5]

squares = [i**2 for i in num_list]
print(squares)
#출력: [1, 4, 9, 16, 25]
```

<br>

### 리스트의 정렬 방법

리스트를 정렬하기 위해 `sort()` 메서드나 `soted()` 함수를 사용할 수 있습니다. sort() 메서드는 원본 리스트를 정렬하지만, sorted() 함수는 정렬된 새로운 리스트를 반환합니다.

```python
num_list = [2, 13, 5, 0, 24]

num_list.sort()
print(num_list)
#출력: [0, 2, 5, 13, 24]

new_list = sorted([5, 4, 3, 2, 1])
print(new_list)
#출력: [1, 2, 3, 4, 5]
```

<br>

### 리스트를 활용한 검색

리스트에서 특정 값을 찾기 위해 `index()` 메서드나`in` 키워드를 사용할 수 있습니다. index() 메서드는 찾고자 하는 값의 첫 번째 위치를 반환하며, in 키워드는 값이 리스트에 있는지 여부를 반환합니다.

```python
num_list = [1, 2, 3, 4, 5]

print(num_list.index(3)) #출력: 2
print(3 in num_list) #출력: True
```


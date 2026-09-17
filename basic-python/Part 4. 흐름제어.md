흐름제어라 하면은 조건문, 반복문, 예외처리 같은 것을 말함
프로그램이 실행되는 동안 명령문이나 코드 블록 등의 실행 순서를 제어하고 결정하는 프로그래밍 개념

# 흐름 제어의 종류
## 조건문
조건을 검사하고 그 결과에 따라 실행
- 프로그램은 다양한 명령문들의 집합
- 언제 어떠한 명령문을 사용할 것인가
- 다양한 분기와 선택, 논리 구조의 구현

- 만약 (if)와 그렇지 않다면 (else)로 구성
- if 뒤에는 참/거짓을 가지는 조건문
- else 뒤에는 조건이 작성되지 않음
```python
if{boolean statement}:
	...
```
- 조건에 의해 수행될 명령은 indent로 구분
### 복합 조건문
- 여러 조건들을 중첩하여 체크하는 경우
- 한 if에서 필터링이 되지 않는 경우
- 여러 조건을 동시에 만족해야 하는 경우
- 계층 구조에 따른 조건문을 만들고 싶은 경우
```python
elif {boolean statement}:
	...
```
if 조건이 성립하지 않으며, 새로운 조건을 만족할 때 수행.
즉, 참 / 거짓 뿐만 아니라 제 3의 조건인 경우

```python
if {boolean statement} [and / or] {boolean statement}:
	...
```
논리 연산을 거친 결과가 True인 경우

# 실습 
<img width="1297" height="224" alt="image" src="https://github.com/user-attachments/assets/45621b35-1077-4c85-8f8b-482f19ad4bf1" />



왜 `a == b` 을 써야 할까? 왜 is는 좋지 않다고 하는 걸까?
일단 `a == b`는 값이 같은가? 를 비교하게 되고 `a is b`는 두 개가 같은 객체인가?를 판단하게 된다.
```
a = "흐림"
b = "".join(["흐", "림"])

print(a == b)  # True
print(a is b)  # False일 수 있음
```
이런 식으로 합체해서 붙이는 경우에는 두 가지를 다른 객체로 보게 될 수도 있다.

엥? 그러면 객체를 판단한다는 건 뭘까? 값으로 판단하는 것이 아니라면?
변수는 알다시피 선언될 때 어떤 메모리 값을 가지게 된다. 즉, 이 두 개의 변수가 같은 메모리 주소를 가리키고 있다면 '같은 객체'라고 판단할 수 있게 되는 것이다.

따라서
```
a = 1
b = a
```
라면 `a is b`는 True가 된다. 

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3dad0f1f-4e6f-45d6-adf7-d051db79d009" />


## 반복문
어떤 코드 블럭을 반복해서 실행
- "다른 값"에 대한 "동일한 연산"을 수행
- 자동적이고 효율적으로 반복 수행할 수 있음

### for문
- for: 시퀀스 (리스트, 튜플, 문자열 등)을 순회할 수 있음
	- 시퀀스: 반복 가능한 (Next 요소가 있는) 저장공간
- for을 통해 시퀀스 요소들에 동일한 연산을 수행
- 고정된 수행횟수
	- 반복하여 수행될 명령은 indent(들여쓰기)로 구분

```python
for {변수명} in {시퀀스}:
else:
```
for문에서 else는 반복문이 다 돌고 난 다음에 나오게 됨

- 특정 횟수를 반복하고 싶다면 `range()`라는 메소드를 이용하면 됨. 범위 지정도 되고, 그 중간 중간 차이? 도 만들어줄 수 있고 1, 3, 5, 7, ... 처럼 가게 만들 수 있고 
- `enumerate()`를 이용해서 시퀀스를 순회하며, 요소와 인덱스 쌍을 튜플로 반환할 수 있음.
	- 요소와 위치를 동시에 활용할 수 있음
	- for loop의 시퀀스를 enumerate()로 감싸서 사용 
### while문
- 조건이 True인 동안 반복
- 수행 횟수가 고정되지 않음
	- 반복하여 수행될 명령은 indent로 구분
- 반복문 내부에서 상태의 변화를 만들어주거나, 종료될 수 있는 상황을 만들어줘야 함
```python
while {boolean_statement}:
else:
```
얘도 마찬가지로 이 while문이 끝나면 else문에 있는 게 실행되는 구조

반복문 제어하기
- break, 현재 수행 중인 반복문을 중단
- continue, 이 순회를 여기서 멈추고 다음 순회를 시작

#### 무한 루프
`while True`
- 이 loob는 프로그래머가 작성한 종료 규칙 또는 강제 중지로만 종료됨
- 특정 상황에 활용
	- 사용자 입력 대기 상황
	- 실시간 데이터 수집

pass
- 아무 작업도 수행하지 않고 코드 블록을 빠져나오기 위한 예약어
- 아직 구현하지 않은 부분을 나타내거나, 차후 추가하기 위한 목적으로 활용
## 반복문 실습 

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9a63fa27-e4cb-43f4-a947-1f6bad2b79d1" />


<img width="1323" height="148" alt="image" src="https://github.com/user-attachments/assets/c431f6da-2b9d-4be9-9019-7e2d1c20a1c1" />


왜 문제가 됐을까 왜 break와 관련이 있을까
강의 해주시는 분이 그냥 빼먹어버리셨는데 `for-else`문에서 else는 for이 그냥 다 순회해서 끝났을 때 이걸 출력하게 되는 것임. 즉, break문 같은 것으로 중간에 멈추게 해두면 -> else가 안 돌고 그냥 잘 끝나면 else가 나오는 형태였던 것임

만약에 그냥 for문 끝나고 나오는 형태면 그냥 for문 뒤에 print붙이면 되는 거니까. 즉 이런 식의 차이가 존재한다

## 성적관리 프로그램 만들기
- 시나리오
	- 학생 이름을 입력하고 성적을 저장하는 프로그램
	- 성적이 저장된 학생들의 목록을 조회할 수 있다
	- 성적이 저장된 학생의 이름을 입력하변 학점을 조회할 수 있다
	- 각 기능은 메뉴 입력을 통해 선택할 수 있으며 종료 메뉴를 선택하면 프로그램이 종료된다

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0e921b55-3d7f-4fea-8884-ad65cab9f071" />


<img width="1220" height="292" alt="image" src="https://github.com/user-attachments/assets/960aa0e2-7550-4bca-ad07-9d1834a6dbf5" />


이건 별 거 없는 게
key in dict로 적을 수 있는 것을 굳이 왜 key 참조를 한 번 더 하는 것이냐. 같은 느낌? 성능면에서는 당연히 둘 다 딕셔너리 키로 접근이니 O(1)일 테지만, 관례와 가독성 측면에서 이렇게 굳이 적을 필요가 없다는 의미

## 예외처리
- 프로그램 실행 중 발생할 수 있는 예외 (오류) 상황을 처리하는 매커니즘
- 프로그램의 비정상 종료를 막고, 예외 상황에 대한 적절한 조치를 취할 수 있음
- 의도된 예외 발생 및 처리를 통해, 프로그램이 목적에 맞게 동작하도록 구현

구조로는
```python
try:
	{statement} # 예외가 일어날 수 있는 코드
except:
	{statement} # 예외가 일어나면 실행될 코드
else:
	{statement} # 예외가 없을 때 실행될 코드
finally:
	{statement} # 예외 발생 여부와 무관하게 마지막에 실행될 코드
```
파이썬에 정의된 다양한 예외가 있으니까 몇몇가지의 예외를 알고 있으면 효율적 으로 할 수 있을 것

## 예외처리 실습
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/15900a55-bb5c-43b4-b658-555c0b3266b2" />



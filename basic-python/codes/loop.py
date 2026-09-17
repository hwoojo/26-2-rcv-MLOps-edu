# for loop
for i in range(1, 5):
    print(i)
else:
    print("반복이 완료되었습니다.")

# while
i = 0
while i < 5:
    print(i)
    i = i + 1

# ==============

fruits = ["사과", "딸기", "복숭아", "참외"]

for fruit in fruits:
    if fruit == "사과":  # 흐름 제어 안 흐름 제어
        print("사과는 맛있습니다")
    print(f"{fruit}이(가) 과일 바구니에 있습니다.")

# ================
# 무한 루프
while True:
    user_input = input("명령어를 입력해주세요: ")
    if user_input == "exit":
        break
    else:
        pass  # TODO: 차후 개발 예정 // 처럼 표현해 오류 안 나게 가능

# ==============
# 간단한 구구단 연산기 만들어보기. 1-9단, n * 1 ~ n * 9 로 구성되어 있음.
# 즉 반복문 내 반복문이 있는 것
for x in range(1, 10):
    for y in range(1, 10):
        print(f"{x} * {y} = {x * y}")


# =============
# enuemrate 실습
fruits = ["Apple", "Banana", "Blueberry", "Peach"]

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}번째 과일은 {fruit} 입니다.")

# =============
# 팩토리얼 구하기
# n! = n * (n-1) * ... * 2 * 1
# 1부터 늘어나는 형태, 5부터 줄어드는 형태

num = 10
result = 1

for i in range(1, num + 1):
    result = result * i

print(f"{num}!은 {result}입니다.")

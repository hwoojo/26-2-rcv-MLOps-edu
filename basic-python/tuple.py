# 빈 튜플 생성
my_tuple = (1,)  # 빈 튜플 만들기도 가능
fruits = ("apple", "banana", "blueberry")
first = fruits[0]
print(first)  # apple

# 패킹과 언패킹
tp = 1, 2, 3
print(tp)  # (1, 2, 3)

v1, v2, v3 = tp
print(f"{v1}, {v2}, {v3}")

a = 10
b = 20

a, b = b, a  # 이걸로 스왑 구현도 가능
print(a)  # 20

tp2 = (1, 2, 3, 4, 5, 6, 7, 8)
val1, val2, val3, *vals = tp2
print(vals)  # [4, 5, 6, 7, 8] 리스트로 저장된다. *의 특징

val1, val2, val3, *vals, _ = (
    tp2  # 이런 식으로 맨 뒤 것은 무시하게 할 수도 있음. 이러면 8은 버려짐
)
print(vals)  # [4, 5, 6, 7]

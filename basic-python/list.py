my_list = []
my_list.append(10)
my_list.append(15)
my_list.append(20)
print(my_list)  # 10 15 20
print(len(my_list))  # 4


element = my_list[2]
print(element)  # 20

sliced = my_list[1:]
print("sliced: ", sliced)  # 15 20


# =============================================
fruits = ["banana", "apple", "blueberry", "cherry"]

# 바나나가 포함되어 있는가?
is_banana_included = "banana" in fruits
print("Is banana included?", is_banana_included)  # True

# 체리의 위치를 살펴보기
index_cherry = fruits.index("cherry")
print("Cherry is", index_cherry)  # 3
# 없는 값이면? error 발생

# 리스트의 정렬
numbers = [4, 2, 1, 3, 8, 6, 7, 5]
print(numbers)  # 정렬이 안 되어 있음
print(numbers.sort())  # 정렬이 됨
print(numbers.sort(reverse=True))  # 역정렬이 됨

# 리스트의 요소를 추가 및 제거
# 추가는 아까 append를 통해서 했고

numbers.extend([11, 12, 13])
print(numbers)  # 11, 12, 13 추가
numbers.append([14, 15])
print(numbers)  # 14, 15가 리스트로 작용

repeat_list = [1, 2, 3]
print(repeat_list * 2)  # 1, 2, 3, 1, 2, 3

print("max value: ", max(repeat_list))

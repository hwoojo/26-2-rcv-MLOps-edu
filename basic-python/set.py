empty_set = set()  # {}으로 선언할 수 없음. 이러면 딕셔너리가 선언
my_set = {1, 2, 3, 3}  # 이러면 1, 2, 3만 남음

print(my_set)

# ============

fruits = {"apple", "banana", "blueberry"}
print(fruits)  # 위에 그대로 출력

fruits.add("orange")
print(fruits)  # 순서대로 뒤에 붙진 않음

fruits.remove("banana")
print(fruits)  # 삭제 해보기

# =============

fruits1 = {"apple", "strawberry", "peach"}
fruits2 = {"banana", "strawberry", "orange"}

# 합집합
union = fruits1.union(fruits2)
print(union)  # 합집합, 총 5개
print(fruits1 | fruits2)  # 같음

# 교집합
intersection = fruits1.intersection(fruits2)
print(intersection)
print(fruits1 & fruits2)  # 교집합, strawberry

# 차집합
diff1 = fruits1.difference(fruits2)
diff2 = fruits2.difference(fruits1)
print(diff1)  # apple, peach
print(diff2)  # banana, orange
# 순서에 따라서 다르다!

person = {"name": "홍길동", "age": "30", "city": "서울"}
name = person["name"]

print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']}")

# country = person["country"]
# print(f"국적은 {country} 입니다.")
# 이런 식이면 오류가 발생 (없는 키 참조)
country = person.get(
    "country", "알 수 없음"
)  # get을 이용해서 없을 때 기본 출력을 정할 수 있음

print(f"국적은 {country} 입니다.")

# ============================================================

person = {"name": "홍길동", "age": "30", "city": "서울"}
person_detail = {"country": "대한민국", "married": True}
person.update(person_detail)  # 이런 식으로 없는 정보를 업데이트 하게도 할 수 있음

print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']}")

# country = person["country"]
# print(f"국적은 {country} 입니다.")
# 이런 식이면 오류가 발생 (없는 키 참조)
country = person.get(
    "country", "알 수 없음"
)  # 이젠 위에 값을 넣어줬으니 알 수 없음은 나오지 않음

print(f"국적은 {country} 입니다.")

print(person.keys())  # 키 확인. 총 5개의 키가 나온다

del person["married"]

print(person.keys())  # 4개의 키가 나온다

# 기본 매개변수
def welcome(
    city, name="Guest", room=None
):  # 기본 매개변수가 있는 애는 항상 없는 애보다 뒤
    if room == None:
        room = []

    room.append(101)
    print(f"Hello, {name}! This is {city}")


welcome("New York")  # Hello, Guest!
welcome("Seattle", "John")  # Hello, John!


# 키워드 인자
def display_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")


display_info("Alice", 30, "New York")
display_info(city="paris", name="bob", age=22)  # 이러면 순서와 무관하게 입력


# 가변 인자 리스트
def calc_sum(*args):
    total = 0
    for arg in args:
        total += arg  # total = total + arg
    return total


print(calc_sum(1, 2, 3, 4))
print(calc_sum(1, 100))  # 길이가 달라도 문제 없다


# 키워드 가변 인자 리스트
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Eve", age=28, city="Berlin")  # 순서나 길이 상관 없이 가능

info = {"name": "Charlie", "age": 35, "City": "Tokyo"}
print_info(**info)  # 딕셔너리를 만들어서 넣을 때에는 별 두 개!

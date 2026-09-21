def func():
    print("This is function. Hello!")


# 당연히 이것만으로 출력이 되진 않고
func()  # 호출해서 출력을 할 수 있다


def func2(name):
    print(f"This is function. Hello {name}!")


func2("Park")  # 인자는 이런 식으로


def sum(num1, num2):
    return num1 + num2  # 더하기 함수 만들어보기


def div(num1, num2):  # 나누기 함수 만들어보기
    if num2 == 0:
        return 0
    else:  # 있어도 되고 없어도 되고
        return num1 / num2


print(sum(3, 5))
print(div(3, 2))
print(div(1, 0))

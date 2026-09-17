# 문자열 변수 선언
str_var = "this is my python code."
multiline = """this is an example for
    multiline texts """

print(str_var)
print(multiline)

inum1 = 12
inum2 = 23
print(inum1 + inum2)  # 35

snum1 = "12"
snum2 = "23"
print(snum1 + snum2)  # 1223
print(snum1 * 3)  # 121212

# 인덱싱 this is my python code
print(str_var[11])  # p
print(str_var[-1])  # .
print(str_var[-5])  # c
print(str_var[11:17])  # python
print(str_var[11:-6])  # python
print(str_var[:10])  # this is my

# 메소드 사용해보기
print(str_var.isalpha())  # False (공백 문자, 점)
no_space = "thisismypythoncode"
print(no_space.isalpha())  # True

num_var = "12"
print(num_var.isdecimal())  # True

print(str_var.upper())  # THIS IS MY PYTHON CODE.
mixed_text = "This Is With Upper Cases"
print(mixed_text.swapcase())  # tHIS iS wITH uPPER cASES
print(str_var.replace("my", "your"))  # this is your python code

### ========================== ###

# Format String
weather = "흐림"
temp = 15.8

# % code
print("오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp))

# .format()
print("오늘 날씨는 {0} 입니다. 기온은 {1}도 입니다.".format(weather, temp))

# format string
print(f"오늘 날씨는 {weather}입니다. 기온은 {temp + 1}도 입니다.")

# ========================== ###
# 사용자로부터 문자열 입력 받기
print("숫자를 입력해주세요")
num = input()  # 혹은 input("숫자를 입력해주세요")
print(num)

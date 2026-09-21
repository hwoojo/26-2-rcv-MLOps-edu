import math_module

result_add = math_module.add(30, 7)
result_subtract = math_module.subtract(30, 7)
result_multiply = math_module.multiply(30, 7)
result_division = math_module.division(30, 7)

print(
    f"30, 7의 사칙연산 결과: {result_add} {result_subtract} {result_multiply} {result_division}"
)

import calc.basic, calc.advanced

# init에다가 설정을 해두면 . 하고 기능들 적을 필요 없음
# 혹은 __all__ = [] 안에 넣어주는 것으로 * 적는 것으로 다 불러올 수 있게
print(calc.basic.add(3, 7))
print(calc.advanced.div(3, 7))

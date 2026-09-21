# 단일 조건 조건문
value = 30

# 이 값이 20을 초과하는 경우, Big! 이라는 메시지를 출력
if value > 20:
    # print("Big!") 같은 식으로 인덴트가 안 맞으면 실패
    print("Big!")

# 복합 조건문
# 20보다 큰 경우 Big, 그렇지 않은 경우 Small
value = 30
if value > 20:
    print("Big")
else:
    print("Small")

# 50보다 큰 경우 Great, 50보다 작거나 같고 20보다 큰 경우 Big, 그렇지 않은 경우 Small
value = 30
if value > 50:
    print("Great")
elif value <= 50 and value > 20:
    print("Big")
else:
    print("Small")

# 날씨가 흐리고, 강수 확률이 70% 이상이면 비가 온다는 일기예보 만들기
# 필요한 것은 날씨와 강수 확률

condition = "맑음"
rain_rate = 0.70

if condition is "흐림" and rain_rate >= 0.70:
    print("비가 올 확률이 높습니다")
elif condition is "흐림":
    print("날씨가 많이 흐립니다.")
elif condition is "맑음" and rain_rate >= 0.70:
    print("맑지만 비가 올 확률이 높습니다.")
else:
    print("날씨가 좋습니다")

# =============================================
# 사용자로부터 두 개의 값을 입력을 받는다
# 첫 번째 값이 더 크다면 "Win", 두 번째 값이 더 크다면 "Lose"를 출력한다.

# 그렇다면 추가로 입력 값을 숫자로 변환하는 과정이 필요하고
# 두 값이 같을 때에 "Draw"를 출력하는 과정도 필요하다.

var1 = input("첫 번째 값을 입력해주세요: ")
var2 = input("두 번째 값을 입력해주세요: ")

num_var1 = int(var1)
num_var2 = int(var2)

if num_var1 > num_var2:
    print("Win")
elif num_var1 < num_var2:
    print("Lose")
else:
    print("Draw")

# ============================================
# 시험 점수를 입력 받는다. 점수는 1-99점이며 이외의 값이 들어오면 프로그램을 종료한다.
# A: 90-99, B:80-89, C:70-79, D: 60-69, F:-59
# 시험 점수에 맞는 성적을 출력한다

score_str = input("점수를 입력해주세요: ")
score = int(score_str)

if score > 99 or score < 1:
    print("잘못된 입력 값입니다.")
else:
    if score >= 90:
        print("등급은 A입니다.")
    elif score >= 80:
        print("등급은 B입니다.")
    elif score >= 70:
        print("등급은 C입니다.")
    elif score >= 60:
        print("등급은 D입니다.")
    else:
        print("등급은 F입니다.")

# 그러나 이 구조는 작동은 하겠지만 유지보수 측면에서 취약하다
# 새로운 구조를 짜보자

score_str = input("점수를 입력해주세요: ")
score = int(score_str)

if score <= 99 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
elif score <= 79 and score >= 70:
    grade = "C"
elif score <= 69 and score >= 60:
    grade = "D"
elif score <= 59 and score >= 1:
    grade = "F"
else:
    grade = None

if grade is not None:
    print(f"등급은 {grade}입니다.")

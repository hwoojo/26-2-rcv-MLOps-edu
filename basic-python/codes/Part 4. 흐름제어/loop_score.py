students = {}  # 학생-성적이 연결된 형태고, 둘 중 하나를 가지고 조회할 것이므로 딕셔너리
# 입력 대기창
while True:
    # 메뉴 출력
    print("1. 성적 입력하기")
    print("2. 학생 조회하기")
    print("3. 학점 조회하기")
    print("0. 종료하기")
    menu = input("메뉴 번호를 입력하세요: ")
    # 1. 성적 입력하기
    if menu == "1":
        # 학생의 이름과 점수를 입력받아 저장
        name = input("학생의 이름을 입력해주세요: ")
        score = input("학생의 성적을 입력해주세요: ")

        students[name] = int(score)
        print(f"{name}의 성적은 {students[name]}입니다.")
    # 2. 학생 조회하기
    elif menu == "2":
        name = input("조회하고자 하는 학생의 이름을 입력해주세요. ")
        if name in students.keys():
            print(f"{name}의 점수는 {students[name]}입니다.")
        else:
            print(f"{name}은 등록되지 않았습니다.")
    # 3. 학점 조회하기
    elif menu == "3":
        name = input("조회하고자 하는 학생의 이름을 입력하세요: ")
        if name in students.keys():
            pass
        else:
            print(f"{name}은 등록되지 않았습니다.")
            continue

        score = students[name]
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

        if grade in ["A", "B", "C", "D"]:
            mod = score % 10
            if mod >= 5:
                grade = grade + "+"

        print(f"{name}의 학점은 {grade}입니다.")
    # 0. 종료하기
    elif menu == "0":
        break
    else:
        print("잘못된 메뉴가 입력되었습니다.")
        continue

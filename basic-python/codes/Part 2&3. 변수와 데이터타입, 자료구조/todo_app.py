# TodoList를 어떻게 저장할 수 있을까?
# 리스트, 튜플, 세트, 딕셔너리 등과 같은 자료구조 중 뭐가 좋을까?
# 어떤 멤버를 추가하고 삭제하는 자료구조니 불변한 튜플은 안된다
# 리스트나 세트를 쓰는 게 좋아 보인다.
# 만약에 이게 할 일이 좀 더 검색 가능성을 크게 가지려면 딕셔너리를 쓰면 좋겠다
# 교집합이나 차집합 같은 걸 구할 필요는 없으니 리스트가 좋아 보인다.

todo_list = []

while True:
    print("할 일 목록 관리자")
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 할 일 목록 보기")
    print("4. 종료")

    choice = input("선택: ")

    if choice == "1":
        todo = input("추가할 일: ")
        todo_list.append(todo)
        print(f"{todo} 할 일이 추가되었습니다.")
    elif choice == "2":
        todo = input("삭제할 일: ")
        todo_list.remove(todo)
        print(f"{todo} 할 일이 삭제되었습니다.")
    elif choice == "3":
        print(todo_list)
    elif choice == "4":
        break
    else:
        print("올바른 선택이 아닙니다. 다시 시도하세요.")

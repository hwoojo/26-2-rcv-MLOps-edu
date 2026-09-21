# 다이아몬드 상속 만들어보기


class A:
    def method(self):
        print("Method from class A")


class B(A):
    def method(self):
        print("Method from class B")


class C(A):
    def method(self):
        print("Method from class C")


class D(B, C):
    pass


d = D()
d.method()  # 어떤 메서드가 호출될까요?
print(
    D.mro()
)  # mro는 클래스 내장 메소드인데, 이걸 통해서 어떤 순서로 상속을 받고 있는지 알 수 있음

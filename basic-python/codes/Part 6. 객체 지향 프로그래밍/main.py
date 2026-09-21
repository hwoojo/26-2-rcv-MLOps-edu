from programmer import Programmer
from actor import Actor
from farmer import Farmer

people = [
    Programmer("Dave", 42, "Python"),
    Actor("Song", 55, "Parasite"),
    Farmer("Kim", 40, "Apple"),
]

for person in people:
    person.introduce()

# 캡슐화

dave = Programmer("Dave", 42, "Python")
dave.__age = -1  # 같이 하면 직접 접근으로 수정이 되어버림
dave.hello()

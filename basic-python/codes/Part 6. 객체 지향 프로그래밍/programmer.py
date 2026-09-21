from person import Person


class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, job="Programmer")
        self.language = language

    def introduce(self):
        super().hello()
        print(f"나는 {self.language} 언어로 프로그래밍 할 수 있습니다.")

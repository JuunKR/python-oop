class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f'이름: {self.name}, 나이:{int(self.age)}, 성별: {self.sex}')

    def setinfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human('아름', 25, '여자')











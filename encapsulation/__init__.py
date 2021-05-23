class Bmi(object):
    def __init__(self, wieght, hight):
        self.weight = wieght
        self.hight  = hight

    def to_string(self):
        return self.weight / self.hight ** 2 * 1000

    @staticmethod
    def main():
        bmi = Bmi(input('몸무게를 입력하시오  : '), input('키를 입력하시오 : '))
        print(round(bmi.to_string(), 3))

Bmi.main()

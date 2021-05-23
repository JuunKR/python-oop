class Calculator(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def to_string(self):
        return f'더한 값 : {self.first + self.second}\n뺀 값 : {self.first - self.second}\n' \
               f'곱한 값 : {self.first * self.second}\n나눈 값 : {self.first / self.second}'
    @staticmethod
    def main():
        calculator = Calculator(int(input("숫자를 입력하시오 : ")), int(input("숫자를 입력하시오 : ")))
        print(calculator.to_string())


Calculator.main()
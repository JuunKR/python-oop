"""
옵션 있는 계산기 만들기
"""
class Calculator(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add_value(self):
        return self.num1 + self.num2

    def sub_value(self):
        return self.num1 - self.num2


    def mul_value(self):
        return self.num1 * self.num2


    def div_value(self):
        return self.num1 / self.num2

    @staticmethod
    def main():
       while 1:
            menu = int(input('0. 프로그램 종료 1. 더하기 2. 빼기 3. 곱하기 4. 나누기\n : '))
            if menu == 0:
                print('프로그램을 종료합니다.')
                break

            elif menu == 1:
                numbers = Calculator(int(input('첫번째 숫자를 입력하시오 : ')), int(input('두번째 숫자를 입력하시오 : ')))
                print(numbers.num1, '+', numbers.num2, '=', numbers.add_value())

            elif menu == 2:
                numbers = Calculator(int(input('첫번째 숫자를 입력하시오 : ')), int(input('두번째 숫자를 입력하시오 : ')))
                print(numbers.num1, '-', numbers.num2, '=', numbers.sub_value())

            elif menu == 3:
                numbers = Calculator(int(input('첫번째 숫자를 입력하시오 : ')), int(input('두번째 숫자를 입력하시오 : ')))
                print(numbers.num1, '*', numbers.num2, '=', numbers.mul_value())

            elif menu == 4:
                numbers = Calculator(int(input('첫번째 숫자를 입력하시오 : ')), int(input('두번째 숫자를 입력하시오 : ')))
                print(numbers.num1, '/', numbers.num2, '=', numbers.div_value())

            else:
                print('올바른 값을 입력하시오')

Calculator.main()












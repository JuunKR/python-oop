"""
입력 받은 값을 프린트 해보기
"""

def calculator(first, second):
    print(str(number1) + ' + ' + str(number2) + ' = ' +  str(first + second))
    print(number1, '-', number2, '=', first - second)
    print(str(number1) + ' * ' + str(number2) + ' = ' + str(first + second))
    print(number1, '+', number2, '=', first / second)


number1 = int(input("숫자를 입력하시오 : "))
number2 = int(input('숫자를 입력하시오 : '))


calculator(number1, number2)
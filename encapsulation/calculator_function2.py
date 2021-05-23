"""
숫자를 입력받아 한번에 계산
"""
def calculator(first, second):
    print('더한 값 : '+ str(first + second))
    print('뺀 값 :', first - second)
    print('곱한 값 :', first * second)
    print('나눈 값 :', first / second)

calculator(int(input("숫자를 입력하시오 : ")), int(input('숫자를 입력하시오 : ')))







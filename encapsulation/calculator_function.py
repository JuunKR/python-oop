'''
숫자를 한번만 입력받고 그 숫자로 각각 모든 함수를 돌려보고 싶음.
'''

def add_function(first, second):
    return first + second

def sub_function(first, second):
    return first - second

def mul_function(first, second):
    return first * second

def div_function(first, second):
    return first / second


number1 = int(input('숫자를 입력하시오 : '))
number2 = int(input('숫자를 입력하시오 : '))

print(add_function(number1, number2))
print(sub_function(number1, number2))
print(mul_function(number1, number2))
print(div_function(number1, number2))






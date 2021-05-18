'''
이름, 출생년도, 주소를 입력 받아서
회원가입한 사람의 이름, 나이(만), 주소를 출력하시오.
'''

class Person(object):

    pass

if __name__ == '__main__':

    p = Person(input('이름을 입력하시오 : '), int(input('출생년도를 입력하시오 : ')), input('주소를 입력하시오 : '))
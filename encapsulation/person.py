'''
이름, 출생년도, 주소를 입력 받아서
회원가입한 사람의 이름, 나이(만), 주소를 출력하시오.
'''

class Person(object):

    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address

    def age(self):
        return 2021 - self.year - 1

    @staticmethod
    def main():
        p = Person(input('이름을 입력하시오 : '), int(input('출생년도를 입력하시오 : ')), input('주소를 입력하시오 : '))
        print(f'이름 : {p.name}')
        print(f'나이 : {p.age()}')
        print(f'주소 : {p.address}')

Person.main()
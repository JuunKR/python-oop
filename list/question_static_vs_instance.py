import random
'''
인스턴스 메소드와 스태틱 메소드의 차이?
인스턴트를 가져야한다. 안가져와도 된다.
왜 여기서 스태틱을 쓰는가?

ls 질문 
'''
class Account(object):
    '''
    def __init__(self, bank_account, name, money):
        self.BANK_NAME = 'SC은행'
        self.bank_account = bank_account
        self.name = name
        self.money = money

        print(self.BANK_NAME)
    '''

    def instance_number(self):
        ls = [str(random.randint(0,9)) for i in range(2)]
        ls.append('-')
        for i in range(3):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0,9)))
        return "".join(ls)

    @staticmethod
    def static_number():
        ls = [str(random.randint(0, 9)) for i in range(2)]
        ls.append('-')
        for i in range(3):
            ls.append(str(random.randint(0, 9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return "".join(ls)

    @staticmethod
    def main():
        '''
        # 인스턴스 생성
        i = Account()

        print(i.instance_number())

        print(i.static_number())
        '''

        # 인스턴스 생성 X
        print(Account.instance_number(1)) # self 를 안넣을 경우 빨간줄 그어지지만 실행가능, self 를 넣으면 숫자나 문자 넣어야함.

        print(Account.static_number())

Account.main()








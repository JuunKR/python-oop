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

    def instance_number(self): #일단 초록줄이 나오는 것은 파이썬이 이해는 해주지만 정확하지 않음 오류 메시지를 확인하자 한자 vs 한글
                             # 스태틱은 디스크 인스턴스는 메모리 // 일반적으로 메모리가 더 비쌈(매우) 그래서 디스크에 할당하는것이 더 좋음
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








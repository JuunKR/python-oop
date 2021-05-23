import random
'''
인스턴스 메소드와 스태틱 메소드의 차이?
인스턴트를 가져야한다. 안가져와도 된다.
왜 여기서 스태틱을 쓰는가?
'''
class Account(object):

    def __init__(self, bank_account, name, money):
        self.BANK_NAME = 'SC은행'
        self.bank_account = bank_account
        self.name = name
        self.money = money

    def to_string(self):
        return f'은행이름 : {self.BANK_NAME}, 이름: {self.name}, ' \
               f'계좌번호 : {self.bank_account}, 잔액 : {self.money}'

    def create_account_number(self):
        ls = [str(random.randint(0,9)) for i in range(2)]
        ls.append('-')
        for i in range(3):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0,9)))
        return "".join(ls)


    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('------------------------------------------------------------\n'
                         '0. 종료, 1. 개좌개설, 2. 목록확인, 3. 입금, 4. 출금, 5. 계좌삭제\n: ')

            if menu == '0':
                print('프로그램을 종료합니다.')
                break

            elif menu == '1':

                ls.append(Account(Account.create_account_number(1),input('이름 : '), input('초기 잔금 : ')))

            elif menu == '2':
                for i in ls:
                    print(i.to_string())


Account.main()



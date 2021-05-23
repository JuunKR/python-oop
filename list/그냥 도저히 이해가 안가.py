class Account(object):

    def __init__(self, name, money):
        self.BANK_NAME = 'SC은행'
        self.bank_account = '계좌번호'
        self.name = name
        self.money = money

    def __str__(self):
        return "num1 = {}, num2 = {}".format(self.name, self.bank_account)

    def to_string(self):
        return f'은행이름 : {self.BANK_NAME}, 이름: {self.name}, ' \
               f'계좌번호 : {self.bank_account}, 잔액 : {self.money}'

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
                ls.append(Account(input('이름 : '), input('초기 잔금 : ')))

            elif menu == '2':
                for i in ls:
                    print(i.to_string())

        print(ls[0])



Account.main()

'''ls = []
ls.append(1)

print(ls)'''
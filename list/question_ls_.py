'''리스트에 넣은 Account 값 개별로 출력하는법

            elif menu == '3':
                for i, j in enumerate(ls):
                    account_number = ('계좌번호 : ')
                    money = input('입금할 금액 : ')
                    if j.bank_account == account_number
                        pass

j 는 어떻게 ACCOUNT에 접근?


'''


class Account(object):

    def __init__(self, account_number, name, money):
        self.BANK_NAME = 'SC은행'
        self.name = name
        self.account_number = account_number
        self.money = money

    def to_string(self):
        return self.name

    @staticmethod
    def main():
        a = Account()
        ls = []   #객체를 여기에.. .

        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌내용 3.입금 4.출금 5.계좌탈퇴')
            if menu == '0':
                break
            elif menu == '1':

                ls.append(Account("name",
                                  input('name'),
                                  input('money')))
                print(a.account_number)



                ### print(f'{}님의 계좌번호는 {}입니다.')
            elif menu == '2':
                for i in ls:
                    print(i.to_string())


Account.main()


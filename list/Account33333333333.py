import random

class Account(object):
    def __init__(self, name, money):
        self.BANK_NAME = 'SC은행'
        self.name = name
        self.account_number = self.create_account_number()
        self.money = money
    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''
    def create_account_number(self):
        ls = []
        for i in range(3):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0,9)))
        return "".join(ls)

    def to_string(self):
        return f'Bank Name : {self.BANK_NAME}, Name : {self.name}, ' \
               f'Account Number : {self.account_number}, Money : {self.money} '

    @staticmethod
    def main():

        while 1:
            menu = input('0.Exit 1.Create 2.Read 3.Update 4.Delete')
            if menu == '0':

                account = Account(None,
                                  None)
                print(account.create_account_number())
                break



            elif menu == '1':
                account = Account(input('BANK_NAME'),
                                  input('name'),
                                  input('account_number'),
                                  input('money'))


            elif menu == '2':
                print(account.to_string())

            elif menu == '3':
                account = Account(account.BANK_NAME,
                                  account.name,
                                  account.account_number,
                                  input('money'))


            elif menu == '4':
                account = None


Account.main()






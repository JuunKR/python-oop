class Account(object):
    def __init__(self, BANK_NAME, name, account_number, money):
        self.name = name
        self.money = money
        self.BANK = BANK_NAME
        self.account_number = account_number

    def to_string(self):
        return f'Bank Name : {self.BANK_NAME}, Name : {self.name}, ' \
               f'Account Number : {self.account_number}, Money : {self.money}  '


    @staticmethod
    def main():

        while 1:
            menu = input('0.Exit 1.Create 2.Read 3.Update 4.Delete')
            if menu == '0':
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






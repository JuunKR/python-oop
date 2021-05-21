import random

class Account(object):
    def __init__(self, account_num, name, money):
        self.BANK_NAME = 'SC은행'
        self.name = name
        self.account_num = account_num
        self.money = money


    @staticmethod
    def create_account_num():
        create_ls = [str(random.randint(0, 9)) for i in range(3)]
        create_ls.append('-')
        for i in range(2):
            create_ls.append(str(random.randint(0, 9)))
            create_ls.append('-')
        for i in range(6):
            create_ls.append(str(random.randint(0, 9)))



    @staticmethod
    def to_string(self):
        return f'은행이름: {self.BANK_NAME},' \
           f'이름: {self.name}' \
           f'계좌번호: {self.account_num}' \
           f'잔액: {self.money}'


    @staticmethod
    def main():
        ls=[]
        while 1:
            menu = input("0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.삭제")

        if menu == 0:
            print('프로그램을 종료합니다.')
            break

        elif menu == 1:
            ls.account = Account(input("이름:"), input("금액: "))

        elif menu == 2:
            for i in ls:
                pass
        elif menu == 3:
            pass
        elif menu == 4:
            pass
        elif menu == 5:
            pass
        else:
            print('올바른 값을 입력하시오.')




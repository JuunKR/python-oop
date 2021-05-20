import random

class Account(object):

    def __init__(self, person_name, balance):
        self.bank_name = 'sc은행'
        self.person_name = person_name
        self.balance = balance
        self.x1 = random.randrange(100,999)
        self.x2 = random.randrange(1,99)
        self.x3 = random.randrange(100000,999999)
    def get_account(self):
        return f'은행이름 : {self.bank_name}, 예금주 : {self.person_name}, 계좌번호 : {self.x1}-{self.x2}-{self.x3}, 잔액 : {self.balance} '


    @staticmethod
    def main():
        ls = []
        while 1:
            option = input('\n0. 종료\n'
                         '1. 입력\n'
                         '2. 출력\n'
                         '3. 수정\n'
                         '4. 삭제\n' 
                         ': ')
            if option == '0':
                print('프로그램을 종료합니다.')
                break

            elif option == '1':
                ls.append(Account(input('이름 : '), input('잔고 : ')))

            elif option == '2':
                for i in ls:
                    print(f'출력결과 : {i.get_account()}')

            elif option == '3':
                edit_name = input('수정할 이름 : ')
                edit_info = Account(edit_name, input("수정잔고 : "))
                for i, j in enumerate(ls):
                    if j.person_name == edit_name:
                        del ls[i]
                        ls.append(edit_info)

            elif option == '4':
                edit_name = input('삭제할 이름 : ')
                for i, j in enumerate(ls):
                    if j.person_name == edit_name:
                        del ls[i]
            else:
                print('올바른 값을 입력해 주시오.')
                continue    

Account.main()


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


    @staticmethod
    def create_account_number():
        ls = [str(random.randint(0,9)) for i in range(2)]
        ls.append('-')
        for i in range(3):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0,9)))
        return "".join(ls)

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.bank_account == account_number:
                del ls[i]




    @staticmethod
    def main():
        ls = []
        account_count = 0

        while 1:
            menu = input('------------------------------------------------------------\n'
                         '0. 종료, 1. 개좌개설, 2. 목록확인, 3. 입금, 4. 출금, 5. 계좌삭제\n: ')

            if menu == '0':
                print('프로그램을 종료합니다.')
                break

            elif menu == '1':

                account = Account(Account.create_account_number(), input('이름 : '), int(input('초기 잔금 : ')))
                print(f'{account.name}님의 계좌번호는 {account.bank_account}이며 잔액은 {account.money}원 입니다')
                ls.append(account)
                account_count += 1

                '''account = Account(Account.create_account_number(), input('이름 : '), int(input('초기 잔금 : ')))

                try:
                    if account.money >= 0:
                        print(f'{account.name}님의 계좌번호는 {account.bank_account}이며 잔액은 {account.money}원 입니다')
                        ls.append(account)
                        account_count += 1

                    else:
                        print('0원 이상의 값을 입력해 주세요.')

                except ValueError:
                    print('0원 이상의 값을 입력해 주세요')'''


            elif menu == '2':
                for i in ls:
                    print(i.to_string())

            elif menu == '3':
                account_number = input('입금할 계좌번호 : ')
                money = int(input('입금할 금액 : '))
                count = 0
                for i, j in enumerate(ls):
                    if money > 0:
                        if j.bank_account == account_number:
                            opt = input(f'{j.name}님에게 입금하시겠습니까?\n'
                                        f'송금 0, 취소 1\n: ')
                            if opt == '0':
                                replace = Account(j.bank_account, j.name, int(j.money) + int(money))
                                Account.del_account(ls, account_number)
                                ls.append(replace)
                            else:
                                continue

                        elif j.bank_account != account_number:
                            count += 1
                            if count == account_count:
                                print("없는 계좌번호입니다.")
                    else:
                        print('0원 이상의 값을 입력해주세요')


            elif menu == '4':
                account_number = input('출금할 계좌번호 : ')
                money = int(input('출금할 금액 : '))
                for i, j in enumerate(ls):
                    if j.money - money >= 0:
                        if j.bank_account == account_number:
                            opt = input(f'{money}원을 출금하시겠습니까?\n'
                                        f'출금 0, 취소 1\n: ')
                            if opt == '0':
                                replace = Account(j.bank_account, j.name, int(j.money) - int(money))
                                Account.del_account(ls, account_number)
                                ls.append(replace)
                            else:
                                continue

                        elif j.bank_account != account_number:
                            count += 1
                            if count == account_count:
                                print("없는 계좌번호입니다.")
                    else:
                        print(f'{money}원 이상 출금할 수 없습니다.')

            elif menu == '5':
                Account.del_account(ls, input('삭제할 계좌번호 : '))
                account_count -= 1

            else:
                print('올바른 값을 입력하시오')
                continue



Account.main()



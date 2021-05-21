import random
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

    def get_info(self):
        return f'은행 : {self.bank}, 예금주 : {self.name}, 계좌번호 : {self.account_number}, 초기 잔액: : {self.balance}'

    @staticmethod
    def main():
        ls = []
        while 1:
            opt = int(input('\n종료 : 0\n'
                        '입력 : 1\n'
                        '출력 : 2\n'
                        '수정 : 3\n'
                        '삭제 : 4\n'
                        '입금 : 5\n'))
            if opt == 0:
                print('프로그램을 종료합니다.')
                break

            elif opt == 1:
               ls.append(Account(input('이름 : '), input('잔금 : ')))

            elif opt == 2:
                for i in ls:
                    print(i.get_info())

            elif opt == 3:
                edit_name = input('수정할 이름 : ')
                edit_info = Account(edit_name, input('수정할 잔고 : '))
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)

            elif opt == 4:
                del_name = input('삭제할 이름 : ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]

            elif opt == 5:
                deposit_name = input('입금자 성함 : ')
                deposit = int(input('입금할 금액 : '))
                for i, j in enumerate(ls):
                    if j.name == deposit_name:
                        ls.append(deposit)
                        print(ls)


            else:
               print('올바른 값을 입력하시오.')

Account.main()



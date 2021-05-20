class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code


    def get_stock(self):
        return f'종목명 : {self.name}, 종목코드 : {self.code}'


    @staticmethod
    def main():
        while True:
            option = input('\n0. 종료\n'
                         '1. 입력\n'
                         '2. 출력\n'
                         ': ')
            if option == '0':
               print('프로그램을 종료합니다.')
               break

            elif option == '1':
               s = Stock(input('\n종목명 : '), input('종목코드 : '))

            elif option == '2':
                print(s.get_stock())

            else:
                print('잘못된 옵션을 선택했습니다.')
                continue

Stock.main()
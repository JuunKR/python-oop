class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code


    def to_string(self):

        return f'종목명 : {self.name}, 종목코드 : {self.code}'

    @staticmethod
    def del_element(ls, edit_stock):
        for i, j in enumerate(ls):
            if j.code == edit_stock:
                del ls[i]


    @staticmethod
    def main():

        ls = []

        while True:
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
               ls.append = Stock(input('\n종목명 : '), input('종목코드 : '))

            elif option == '2':
                for i in ls:
                    print(f'출력결과 : {i.to_string()}')


            elif option == '3':
                edit_stock = input('종목 이름 : :')
                stock = Stock((input('수정할 이름'), edit_stock))
                stock.del_element(ls, edit_stock)
                ls.append(stock)

            elif option == '4':
                stock = Stock(None, input("수정잔고 : "))
                stock.del_element(ls, input('종목이름'))

            else:
                print('잘못된 옵션을 선택했습니다.')
                continue

Stock.main()
class Account(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    @staticmethod


    def main():
        ls = []
        while 1:
            menu = int(input('\n종료 : 0\n'
                        '입력 : 1\n'
                        '출력 : 2\n'
                        '수정 : 3\n'
                        '삭제 : 4\n'))

            if menu == 0:
                print('프로그램을 종료합니다.')
                break

            if menu == 1:
               ls.append=Account(input('이름을 입력하시오 : '), ('종목코드를 입력하시오 : '))




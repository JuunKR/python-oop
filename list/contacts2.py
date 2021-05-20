'''
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''

class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_contact(self):
        return f'이름 : {self.name}, 전화번호 : {self.phone}, 이메일 : { self.email}, 주소 : {self.address}'

    @staticmethod
    def main():

        ls = []
        while 1:
            opt = int(input('\n종료 : 0\n'
                        '입력 : 1\n'
                        '출력 : 2\n'
                        '수정 : 3\n'
                        '삭제 : 4\n'))
            if opt == 0:
                print('시스템을 종료합니다.')
                break
            elif opt == 1:
               ls.append(Contacts(input("이름 : "), input('전화번호 : '), input('이메일 : '), input('주소 : ')))
            elif opt == 2:
               for i in ls:
                   print(f'출력결과 : {i.get_contact()}')

            elif opt == 3:
                edit_name = input("수정할 이름 : ")
                edit_info = Contacts(edit_name, input('수정할 번호 : '), input('수정할 이메일 : '), input('수정할 주소 :'))
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)

            elif opt == 4:
                del_name = input("삭제할 이름 : ")
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]

            else:
                print('올바른 값을 입력하시오.')



Contacts.main()

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
        return f'이름 : {self.name}, 전화번호 : {self.phone}, 이메일 : {self.email}, 주소 : {self.address}'


    @staticmethod
    del del_element(ls,edit_name):
        pass




    @staticmethod
    def main():
        ls = [  ]
        while 1:
            menu = int(input("\n옵션을 선택해 주세요 \n"
                             "0. 프로그램 종료\n"
                             "1. 주소록 추가\n"
                             "2. 출력\n"
                             "3. 삭제\n"
                             "4. 수정\n"
                             "--> "))


            if menu == 0:
                print("프로그램을 종료합니다.")
                break

            elif menu == 1:
                 ls.append(Contacts(input('이름 : '), input('전화번호 : '), input('이메일 : '), input('주소 : ')))

            elif menu == 2:
                for i in ls:
                    print(f'출력결과 : {i.get_contact()}')
            elif menu == 3:
                account.del_element(ls, input('삭제할 이름 : '))


            elif menu == 4:
                edit_name = input('수정할 이름 : ')
                edit_info = Contacts(edit_name, input('수정 전화번호'), input('수정 이메일'), input('수정 주소'))
                account.del_element
                ls.append(edit_info)
            else:
                print('잘못된 주문입니다.')
                continue


Contacts.main()







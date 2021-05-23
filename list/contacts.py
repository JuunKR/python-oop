'''
같은 이름의 변수를 만들어도 되는지
'''

'''
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''
class Contacts(object):
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address

    def to_string(self):
         return f'이름: {self.name}, 전화번호: {self.phone}, 주소: {self.address} '


    @staticmethod
    def main():
        ls = []
        count = 0
        while 1:
            menu = input('0.종료, 1.정보입력, 2.목록 3.정보수정 4.삭제\n: ')

            if menu == '0':
                print('프로그램을 종료합니다.')
                break
            if menu == '1':
                ls.append(Contacts(input('이름 : '), input('전화번호 : '), input('주소 : ')))
                print('정보입력이 완료되었습니다.')
                count += 1
            elif menu == '2':
                print('회원정보')
                for i in ls:
                    print(i.to_string())

            elif menu == '3':
                info_number = 0
                name = input('정보수정을 원하는 이름를 입력하시오.\n: ')
                for i, j in enumerate(ls):
                    info_number += 1
                    if name == j.name:
                        info = input('수정을 원하는 정보를 선택해주세요.\n'
                              '0.이름 1.전화번호 2.주소\n: ')
                        if info == '0':
                            change_name = input('변경된 이름을 입력하시오.\n: ')
                            opt = input(f'{j.name}을 {change_name}으로 변경하시겠습니까?\n'
                                                '0.변경, 1.취소\n: ')
                            if opt == '0':
                                replace = Contacts(change_name, j.phone, j.address)
                                del ls[i]
                                ls.append(replace)
                                print('이름 변경이 완료되었습니다.')
                                break
                            elif opt == '1':
                                print('이름 변경이 취소되었습니다.')
                                break
                            else:
                                print('올바른 값을 입력하시오.')
                                break

                        elif info == '1':
                            change_phone = input('변경된 전화번호를 입력하시오.\n: ')
                            opt = input(f'{j.phone}을 {change_phone}으로 변경하시겠습니까?\n'
                                                '0.변경, 1.취소\n: ')
                            if opt == '0':
                                replace = Contacts(j.name, change_phone, j.address)
                                del ls[i]
                                ls.append(replace)
                                print('전화번호 변경이 완료되었습니다.')
                                break
                            elif opt == '1':
                                print('전화번호 변경이 취소되었습니다.')
                                break
                            else:
                                print('올바른 값을 입력하시오.')
                                break

                        elif info == '2':
                            change_address = input('변경된 주소를 입력하시오.\n: ')
                            opt = input(f'{j.address}을 {change_address}으로 변경하시겠습니까?\n'
                                        '0.변경, 1.취소\n: ')
                            if opt == '0':
                                replace = Contacts(j.name, j.phone, change_address)
                                del ls[i]
                                ls.append(replace)
                                print('주소 변경이 완료되었습니다.')
                                break
                            elif opt == '1':
                                print('주소 변경이 취소되었습니다.')
                                break
                            else:
                                print('올바른 값을 입력하시오.')
                                break

                        else:
                            print('올바른 값을 입력하시오.')
                            break

                    elif count == info_number:
                         print('이름을 확인해 주세요.')
                         break
            elif menu == '3':
                del_info = input('삭제를 원하는 정보의 이름을 입력하시오.\n: ')
                for i, j in enumerate(ls):
                    if del_info == j.name:
                        opt = input(f'정말 {j.name}님의 정보를 삭제하시겠습니까?\n'
                                    f'0.삭제, 1.취소\n: ')
                        if opt == '0':
                            del ls[i]
                        elif opt == '1':
                            print('정보삭제가 취소되었습니다.')
                        else:
                            print('올바른 값을 입력하시오.')
                count -= 1
            else:
                print('올바른 값을 입력하시오.')


Contacts.main()







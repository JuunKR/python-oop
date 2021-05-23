'''
main vs static
'''
class Human(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def get_who(self):
        print(f'이름: {self.name}, 나이:{int(self.age)}, 성별: {self.sex}')

    def set_info(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    '''
    if __name__ == '__main__':
    
        aruem = Human('아름', '25', '여자')
        aruem.get_who()
    '''

    @staticmethod
    def main():
        aruem = Human('아름', '25', '여자')
        aruem.get_who()



Human.main()











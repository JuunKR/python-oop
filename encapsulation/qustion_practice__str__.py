'''
check 안에 인풋받은 값을 한번에 모두 출력해보고 싶음
https://stackoverflow.com/questions/67649873/please-help-me-im-a-beginner-at-python/67649980#67649980
'''
class Check(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return "num1 = {}, num2 = {}".format(self.num1, self.num2)

    @staticmethod
    def main():
        check = Check(int(input(' : ')), int(input(' : ')))

        print('num1 =', check.num1)
        print(check.__str__())

Check.main()
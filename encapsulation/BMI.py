class Bmi(object):
    def __init__(self, hight, weight):
        self.hight = hight
        self.weight = weight

    def to_string(self):
        return self.weight / self.hight ** 2 * 10000

    @staticmethod
    def main():
        user_info = Bmi(int(input('키를 입력하시오 : ')), int(input('몸무게를 입력하시오 : ')))
        bmi = round(user_info.to_string(), 2)
        print(bmi)
        if bmi >= 35:
            print('고도 비만입니다.')

        elif bmi > 30:
             print('중정도 비만입니다.')

        elif bmi > 25:
            print('경도 비만입니다.')

        elif bmi > 23:
            print('과체중입니다.')

        elif bmi >= 18.5:
            print('정상체중입니다.')

        else:
            print('저체중입니다.')

Bmi.main()


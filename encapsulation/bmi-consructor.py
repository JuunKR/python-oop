class Bmi(object):
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def get_bmi(self):
        return int(self.weight / self.height ** 2 * 10000)

    def get_index(self):
        value = self.get_bmi()
        BodyMassIndex= ''

        if value > 35:
            BodyMassIndex = '3단계비만(고도비만)'

        elif value > 30:
            BodyMassIndex = '2단계비만'

        elif value > 25:
            BodyMassIndex = '1단계비만'

        elif value > 23:
            BodyMassIndex = '비만 전 단계'

        else:
            BodyMassIndex = '정상'

        return BodyMassIndex

    @staticmethod
    def main():
        b = Bmi(int(input('키 입력(cm): ')), int(input('몸무게 입력(kg) : ')))
        print(f'BMI 수치 : {b.get_bmi()} ')
        print(f'분류 : {b.get_index()}')

if __name__ == '__main__':
    Bmi.main()




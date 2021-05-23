class Grade(object):
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def get_sum(self):
        return self.kor + self.eng + self. math

    def get_avg(self):
        return self.get_sum() / 3

    @staticmethod
    def main():
        score = Grade(int(input('국어 점수 : ')), int(input('영어 점수 : ')), int(input('수학 점수 : ')))
        avg = score.get_avg()

        if avg > 90:
            print('A학점 입니다.')

        elif avg > 80:
            print('B학점 입니다.')

        elif avg > 70:
             print('C학점 입니다.')

        elif avg > 60:
            print('D학점 입니다.')

        elif avg > 50:
            print('E학점 입니다.')

        else:
            print('F학점 입니다.')


Grade.main()









class Grade:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

if __name__ == '__main__':
    g = Grade(50, 50, 100)
    print(g.sum())
    print(g.avg())
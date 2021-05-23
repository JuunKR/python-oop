class Bmi(object):
    def __init__(self, hight, weight):
        self.hight = hight
        self.weight = weight

    def to_string(self):
        return self.weight / self.hight**2 * 10000



    @staticmethod
    def main():
        bmi = Bmi(170, 62)
        print(round(bmi.to_string(), 2))

Bmi.main()
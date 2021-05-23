class Bmi(object):
    def set_info(self, hight, weight):
        self.hight = hight
        self.weight = weight

    def get_info(self):
        return self.weight / self.hight ** 2 * 10000


if __name__ == '__main__':
    bmi = Bmi()
    bmi.set_info(176, 62)
    print(round(bmi.get_info(), 2))

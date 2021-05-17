class Bmi:
    def set_info(self, W, H1, H2):
        self.W = W
        self.H1 = H1
        self.H2 = H2

    def result(self):
        return self.W / (self.H1 * self.H2)

if __name__ == '__main__':
        b = Bmi()
        b.set_info(63, 1.76, 1.76)

        print(b.result())

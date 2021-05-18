class Bmi:
    def set_info(self, W, H):
        self.W = W
        self.H = H


    def result(self):
        return self.W / (self.H ** 2)

if __name__ == '__main__':
        b = Bmi()
        b.set_info(63, 1.76)

        print(b.result())

def add_fuction(first, second):
    return first + second

def sub_fuction(first, second):
    return first - second

def mul_fuction(first, second):
    return first * second

def div_fuction(first, second):
    return first / second


class Calculator:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

if __name__ == '__main__':
   '''
   # c = Calculator()
   # c.setdata(1, 2)

   # print(c.add())
   # print(c.sub())
   # print(c.mul())
   # print(c.div())
   '''

   addValue = add_fuction(1,3)
   subValue = sub_fuction(1,3)
   mulvalue = mul_fuction(1,3)
   divValue = div_fuction(1,3)

   print(addValue)
   print(subValue)
   print(mulvalue)
   print(divValue)

   print(add_fuction(1,3))1
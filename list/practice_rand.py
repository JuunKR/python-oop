import random
x1 = random.randrange(100,999)
print("3 자리  : " +str(x1))

x2 = random.randrange(1,99)
print("2 자리  : " +str(x2))

x3 = random.randrange(100000,999999)
print("6 자리  : " +str(x3))

print(f'{x1}-{x2}-{x3}')

import random

numbers = []
'''
for i in range(2):
    numbers.append(random.randint(1, 100))

print(numbers)
'''

numbers = [random.randint(1, 100) for i in range(2)]

print(numbers)
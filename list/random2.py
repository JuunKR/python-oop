import random

numbers = []
'''
for i in range(2):
    numbers.append(random.randint(1, 100))

print(numbers)
'''

numbers = [random.randint(1, 100) for i in range(2)]

print(numbers)
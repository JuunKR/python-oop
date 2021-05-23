numbers = []

for i in range(1, 5):
    numbers.append(i)

print(numbers)

numbers = []
for i in range(3):
    numbers.append(i)
    print(numbers)



test = ['A', 'B', 'C']
for i in test:
    print(i)



marks = [90, 25, 67, 45, 80]
number = 0

for i in marks:
    number = number +1
    if i >= 60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다." %number)
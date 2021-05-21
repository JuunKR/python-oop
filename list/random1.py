import random

create_ls = [str(random.randint(0, 9)) for i in range(3)]
create_ls.append('-')
for i in range(2):          # create_ls = [random.randint(0, 9) for i in range(2)]
    create_ls.append(str(random.randint(0,9)))
    create_ls.append('-')
for i in range(6):          # create_ls = [random.randint(0, 9) for i in range(6)]
    create_ls.append(str(random.randint(0,9)))



print("".join(create_ls))

import random
boy = 0
girl = 0
for i in range(1, 100):
    j = random.choice(['1', '0'])
    while j == '1':
        boy += 1
    else:

        s = random.choice(['1', '0'])
        while s == '1':
            boy += 1
        else:
            girl += 1

print(boy,girl)

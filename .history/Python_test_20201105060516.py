import random
boy = 0
girl = 0
for i in range(1, 100):
    j = random.choice(['1', '0'])
    while j == '1':
        boy += 1
    else:

        while True:
            s = random.choice(['1', '0'])
            if s == '1':
                boy += 1

            else:
                girl += 1
            break

print(boy, girl)

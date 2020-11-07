import random
boy = 0
girl = 0
for i in range(1, 1000):
    j = random.choice(['1', '0'])
    if j == '1':
        boy += 1
    else:

        while True:
            s = random.choice(['1', '0'])
            if s == '1':
                boy += 1
                break
            else:
                girl +=1

print(boy, girl)





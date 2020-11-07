import random
boy = 0
girl = 0
second_boy = 0
for i in range(1, 100000):
    j = random.choice(['1', '0'])
    while j == '1':
        boy += 1
        break
    else:

        while True:
            s = random.choice(['1', '0'])
            if s == '1':
                second_boy += 1

                break

            else:
                girl +=1

print(boy+second_boy, girl)





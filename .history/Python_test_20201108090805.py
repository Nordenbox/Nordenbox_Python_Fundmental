"""一个模拟不生出男孩就誓不罢休的模拟器"""

import random
boy = 0
girl = 0
second_boy = 0
for i in range(1, 100000000000000):
    j = random.choice(['1', '0'])
    if j == '1':
        boy += 1
    else:

        while True:
            s = random.choice(['1', '0'])
            if s == '1':
                second_boy += 1

                break

            else:
                girl +=1

print(boy+second_boy, girl)





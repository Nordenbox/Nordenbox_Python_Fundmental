import random
import time


items = input('input how many items : ')
given_items = int(items)
given_list = [random.randint(1,100) for i in range(given_items) ]
print('original list: ', given_list)
A = True
while A:

    if list.sort(given_list) == given_list:
        A = False

    else:
        random.shuffle(given_list)
        time.sleep(0.5)
        print(given_list)






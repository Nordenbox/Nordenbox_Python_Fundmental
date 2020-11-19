import random
import time


items = input('input how many items : ')
given_items = int(items)
given_list = [random.randint(1,100) for i in range(given_items) ]
print('original list: ', given_list)
Sorted = list.sort(given_list)


while True:

    if Sorted == given_list:
        break

    else:
        random.shuffle(given_list)
        time.sleep(2)
        print(given_list)




print(given_list)






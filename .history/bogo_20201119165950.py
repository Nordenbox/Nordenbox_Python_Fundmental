import random
import time


items = input('input how many items : ')
given_items = int(items)
given_list = [random.randint(1,100) for i in range(given_items) ]
print('original list: ', given_list)

while list.sort(given_list) != given_list:

    random.shuffle(given_list)
    time.sleep(0.5)
    print(given_list)

print(given_list)






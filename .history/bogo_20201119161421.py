import random


items = input('input how many items : ')
given_items = int(items)

while True:
    given_list = [random.randint(1,100) for i in range(given_items) ]
    if list.sort(given_list) == given_list:
        break


    print(given_list)


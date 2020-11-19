import random


items = input('input how many items : ')
given_items = int(items)
given_list = [random.randint(1,100) for i in range(given_items) ]
print('original list: ', given_list)
while True:

    if list.sort(given_list) == given_list:
        continue
    else:
        random.shuffle(given_list)
        print(given_list)





import random


items = input('input how many items : ')
given_items = int(items)
given_list = [random.randint(1,100) for i in range(given_items) ]
print('original list: ', given_list)
while True:

    a= list.sort(given_list)

    if  a == given_list:
        break
    else:
        b = random.shuffle(given_list)
        if list.sort(b) == b:
            print(b)
            break





import random


items = input('input how many items')
given_items = int(items)
given_list = [random.randint(1,100) for i in range(given_items) ]

print(given_list)

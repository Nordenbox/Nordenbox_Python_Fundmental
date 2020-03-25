import random
import time


def findMin(L):
    min = L[0]
    for i in L:
        if i < min:
            min = i
    return min


def my_sort(l):
    sorted_list = []
    for i in range(len(l)):
        sorted_list.append(findMin(l))
        l.remove(findMin(l))
    return sorted_list


a = [random.randint(1, 900000) for i in range(1, 900000)]
print(a, '\n*******************************')
time_start = time.time()
print(my_sort(a))
time_end = time.time()
print(time_end-time_start, 'second')

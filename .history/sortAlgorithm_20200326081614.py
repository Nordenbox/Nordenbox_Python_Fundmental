import random
import time


def findMin(L):  # find a minist element in a certain list
    min = L[0]   # surppose the first element in the list is the minist element
    for i in L:  # map every element of the list
        if i < min:  # if some element is less than surpposed minist, it replace the minist
            min = i
    return min


def my_sort(l):
    sorted_list = []
    for i in range(len(l)):
        sorted_list.append(findMin(l))  # put the minist element into the empty list
        l.remove(findMin(l))  # remove above minist elemnt from original list
    return sorted_list


a = [random.randint(1, 1000) for i in range(1, 300)]
print(a, '\n*******************************')
time_start = time.time()
print(my_sort(a))
time_end = time.time()
print(time_end-time_start, 'second')


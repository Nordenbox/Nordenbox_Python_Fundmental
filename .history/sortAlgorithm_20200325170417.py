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


# a = [random.randint(1, 1000) for i in range(1, 300)]
# print(a, '\n*******************************')
# time_start = time.time()
# print(my_sort(a)[-1])
# time_end = time.time()
# print(time_end-time_start, 'second')

list_unsort = [[1, 2, 5, 1, 3, 1, 5, 2, 6, 1], [4, 5, 3, 4, 5, 2, 4, 1, 6, 4], [4, 3, 1, 5, 4, 4, 6, 5, 6, 6], [3, 1, 1, 3, 5, 3, 4, 2, 3, 3], [6, 3, 6, 6, 2, 5, 5, 5, 6, 2], [4, 4, 5, 3, 3, 1, 1, 1, 4, 4], [3, 4, 6, 2, 6, 2, 3, 2, 6, 6], [3, 1, 4, 6, 4, 4, 6, 1, 6, 6], [3, 3, 3, 5, 2, 3, 2, 5, 1, 2], [2, 3, 2, 5, 6, 2, 5, 5, 1, 6]]
map(list_unsort,my_sort(list_unsort))

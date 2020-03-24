import random


def findMinAndMax(L):
    max = L[0]
    min = L[0]
    for i in L:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min


inputList = [random.randint(1, 99999) for i in range(1, 2399)]
print(inputList)
print(findMinAndMax(inputList))


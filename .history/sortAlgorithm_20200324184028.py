def findMin(L):

    min = L[0]
    for i in L:
        if i < min:
            min = i
    return min

def sort(l):
    sorted_list = []
    for i in range(len(l)):
        sorted_list.append(findMin(l))
        l.remove(findMin(l))
    return sorted_list

sort([random.randint(1,35)] for i in range(1,20))
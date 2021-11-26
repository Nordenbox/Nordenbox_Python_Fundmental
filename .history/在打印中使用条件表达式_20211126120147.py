import collections
list1 = [11, 22, 33, 44, 55]
list2 = [22, 33, 55, 66]
list3 = list1 +list2
list4 = dict(collections.Counter(list3))
print(list4)
print(type(list4))
print([key for key,value in list4.items() if value>1])
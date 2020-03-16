import numpy as np
import random


class MakeRandomList:
    def __init__(self):
        self.Dimentions_rows = Dimentions_rows
        self.Dimentions_columns = Dimentions_columns
        self.random_scale = random_scale

    def creating(self, Dimentions_rows, Dimentions_columns, random_scale):
        Origin_List = []
        for i in range(1, Dimentions_rows + 1):
            Origin_List.append([random.randint(0, random_scale)
                                for i in range(1, Dimentions_columns + 1)])
        return Origin_List
        #    这个地方用了表达式，因为一开始使用的嵌套的 for 循环让我迷失了。

    # for i in range(1, 5):
    #     a.append(random.randint(0, 10))
    #     b.append(a)
    #     其实不用两层循环，一层就可以了。因为 append 函数返回的还是一个列表，包含了原来的列表。


# print(Origin_List)
Dimentions_rows = int(input('how many rows/matrix do you want: '))
Dimentions_columns = int(input('how many columns/matrix do you want: '))
random_scale = int(input('how large the random numbers: '))
numbers_matrix = int(input('how many matrix do you want: '))

creat_list = MakeRandomList()

for s in range(numbers_matrix):
    i = creat_list.creating(Dimentions_rows, Dimentions_columns, random_scale)
    print('No.', s+1, 'Matrix is:\n', np.array(i))
    print('*******')

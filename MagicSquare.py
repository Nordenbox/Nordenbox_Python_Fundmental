''' 这是我写的一个三阶幻方的生成方法，完全用暴力的办法随机计算，
    虽然效率极其低下，但是原理极其简单，不需要设计算法。完全依靠
    CPU暴力生成数字，一个一个去实验。
'''

import random
import time


loops = 0
a = True

time_start = time.time()

while a:    # 定义三阶幻方的每一个方格里的数字是 1-9 的随机整数。
    x1, x2, x3, y1, y2, y3, z1, z2, z3 = (
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9),
    )
    ''' 以下将上下左右与对角线之和相加的算法规定好'''
    row1 = x1 + x2 + x3
    row2 = y1 + y2 + y3
    row3 = z1 + z2 + z3
    column1 = x1 + y1 + z1
    column2 = x2 + y2 + z2
    column3 = x3 + y3 + z3
    diagonal1 = x1 + y2 + z3
    diagonal2 = x3 + y2 + z1

    judge_list = [x1, x2, x3, y1, y2, y3, z1, z2, z3]    
    # 将列表生成，方便后面计算有误重复项。保证无数字重复。
    print("%d+%d+%d=%d" % (x1, x2, x3, row1))
    print("%d+%d+%d=%d" % (y1, y2, y3, row2))
    print("%d+%d+%d=%d" % (z1, z2, z3, row3))
    print("------")
    loops += 1
    if (
        row1 == 15
        and row2 == 15
        and row3 == 15
        and column1 == 15
        and column2 == 15
        and column3 == 15
        and diagonal1 == 15
        and diagonal2 == 15
        and len(judge_list) == len(set(judge_list))    
        # set 函数来生成一个剔除重复项的新列表，和原始列表长度做比较。
    ):

        print("OK!!!!!!计算", loops, "次数之后，生成幻方如下：")
        print(x1, "|", x2, "|", x3)
        print("---------")
        print(y1, "|", y2, "|", y3)
        print("---------")
        print(z1, "|", z2, "|", z3)
        time_end = time.time()
        print("消耗时间", round(time_end - time_start), "秒")
        a = False


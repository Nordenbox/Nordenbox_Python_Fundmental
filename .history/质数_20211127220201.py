'''这里有两个函数，也不一定是函数，而是两个方法，一个是添加元素列表。
一个是是去掉一个列表中所有能整除的元素的方法，简称筛子法。
最关键的问题在于如何理解 break 和 continue 的用处'''


def primeSolutionAppend():
    primenumbers = []  # 设定一个空列表

    for i in range(2, 100): # 除数从头开始一个个试试
        j=2
        for j in range(2, i): # 让被除数从 2 开始，一直到除数，每一个都试一遍。
            if (i % j == 0): # 如果能被整除
                break   # 这个地方很重要，就是跳出 for 循环，不继续了。换下一个除数。
        else:           # # 这个 else 我还没看太懂，应该不在 for 循环里。
            primenumbers.append(i)  # 不能被整除的话就添加到列表中
    print(primenumbers)
    
def primeSolutionRemove():  # 采用取出某些元素的办法
    original_temp = [s for s in range(2, 100)]   # 现有一个列表，这里是 1-100

    for i in range(2, 100):   # 除数从 2 开始到 100，但是注意，这里的 i 不在那个列表里，独立存在
        for j in range(2, i):  # 被除数就是从 2 开始一直到除数，一个个被除，看看
            if i % j == 0:     # 能不能被整除，如果能，则不是质数。
                original_temp.remove(i)   # 从那个原始列表里删除这个元素。
                break               # 这个地方很重要，break 表示跳出 for 循环

            else:
                pass    # 这个地方用 continue 也可以，其实也需要好好想想，因为这个地方应该不做处理即可。

    print(original_temp)
    

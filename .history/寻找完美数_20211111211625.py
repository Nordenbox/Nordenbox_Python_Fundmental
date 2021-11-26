"""寻找给定范围的完美数。"""

import math  # 导入数学函数库 ceil 要用。

def Judge(x):  # 写一个函数，判断一个数是不是完全数。
    factorlist=[]  # 设计一个空空如也的列表
    for i in range(1,math.ceil(x/2+1)):  # 在给定数字的二分之一处循环，因为大约二分之一的数字不可能是质因子）
        if x%i ==0:  # 这个数除以之前的每一个数，然后没有余数，即整除……则就是质因子
            factorlist.append(i) # 添加到一个质因子列表中。不包含自身。

    if sum(factorlist)==x: # 跳出循环，判断这个质因子列表的各项综合是否是该数字。之前这个判断语句写在了上面循环中，错。

        return True
    else:
        False
Perfect=[]
for j in range(1,100000): # 在一个给定的范围里，逐一试试。
    if Judge(j)== True:
        Perfect.append(j)
print(Perfect)

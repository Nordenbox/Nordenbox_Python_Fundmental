'''计算20个人生日重合的概率'''

import random

t = 0 # 计数器归零

for i in range(100000):  # 重复实验的次数
    s = [random.randint(1, 365) for j in range(20)] # 生成一个由365天的数字构成的列表，列表元素20个。
    if len(set(s)) != len(s): # 比较这个列表有没有重复元素，如果有就计数器加一
        t = t + 1

print(t / 100000)  #  算出百分比

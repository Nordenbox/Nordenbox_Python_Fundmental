'''
一个效率极其低下的排序算法，俗称猴子排序。
原理即不断随机排序原有给定列表，直到出现刚刚好为止。
其时间有可能是无限长。
需要排序的元素个数 2-8 的时间都很快，但 9-10 就慢下来。
10 以上将不可预测。
一切取决于你的运气。
因为运气足够坏的话，即使两个元素，
也会出现很多次都不能刚好排序的情况。
'''

import random
import time


items = input('输入列表包含多少元素 : ')
given_items = int(items)
given_list = [random.randint(1,100) for i in range(given_items) ]
print('原始列表为： ', given_list)
t=0
start_time = time.time()
while sorted(given_list) != given_list:   # 检查这个随机生成的列表是否是良序。
                                          # 如果不是，就进入循环。大概率不是。


    random.shuffle(given_list)   # 随机再次胡乱排序。运气。shuffle 无返回值，直接改变原来列表。

    #print(given_list)
    t=t+1
end_time = time.time()
print('---------------------')

print(given_list)
print('消耗时间 = ', end_time-start_time, '秒')
print('一共排序',t,'次')






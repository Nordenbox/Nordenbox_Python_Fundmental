'''
一个效率极其低下的排序算法，俗称猴子排序。
原理即不断随机排序原有给定列表，直到出现刚刚好为止。
其时间有可能是无限长。
2-7 的时间都很快，但 8-9 就慢下来。
10 以上将不可预测。
'''

import random
import time


items = input('input how many items : ')
given_items = int(items)
given_list = [random.randint(1,100) for i in range(given_items) ]
print('original list: ', given_list)
start_time = time.time()
while sorted(given_list) != given_list:


    random.shuffle(given_list)

    print(given_list)
end_time = time.time()
print('---------------------')
print(given_list)
print('Time lapse = ', end_time-start_time, 'seconds')






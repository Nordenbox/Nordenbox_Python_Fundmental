'''一个效率极其低下的排序算法，俗称猴子排序。'''

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
print(given_list)
print('Time lapse = ', end_time-start_time, 'seconds')






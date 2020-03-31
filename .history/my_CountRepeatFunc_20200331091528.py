"""模拟以下的代码和 Counter 函数。

from collections import Counter  # 引入Counter

a = [29, 36, 57, 12, 79, 43, 23, 56, 28, 11, 14, 15, 16, 37, 24, 35, 17, 24, 33, 15, 39, 46, 52, 13]
b = dict(Counter(a))

print([key for key, value in b.items() if value > 1])  # 只展示重复元素
print({key: value for key, value in b.items() if value > 1})  # 展现重复元素和重复次数

# [15, 24]
# {15: 2, 24: 2}

"""
import random


def count_repeat_elements(list_given):
    dict_key_values_repeat = {}
    repeat_count = []
    for i in list_given:
        for j in list_given[0:list_given[i]]:
            if i in list_given[0:list_given[i]]:
                repeat_count.append(i)

            dict_key_values_repeat[key:value]= (i,len(repeat_count))


        return dict_key_values_repeat

list_given = [random.randint(1,100) for i in range(1,200)]
print(count_repeat_elements(list_given))
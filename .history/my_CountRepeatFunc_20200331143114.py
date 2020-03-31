"""模拟以下的代码和 Counter 函数。找到一个列表中重复的元素和重复次数。

from collections import Counter  # 引入Counter

a = [29, 36, 57, 12, 79, 43, 23, 56, 28, 11, 14, 15, 16, 37, 24, 35, 17, 24, 33, 15, 39, 46, 52, 13]
b = dict(Counter(a))

print([key for key, value in b.items() if value > 1])  # 只展示重复元素
print({key: value for key, value in b.items() if value > 1})  # 展现重复元素和重复次数

# [15, 24]
# {15: 2, 24: 2}

"""
import random


def my_counter_function(list_given):  # 我的函数
    dict_key_values_repeat = {}  # 建立一个空字典
    for i in list_given:   # 遍历列表中的每一个元素
        s=0                # 这个计数器只能在循坏开始后初始化，每次循环均清零。
        for j in list_given:   # 对每一个元素，重新遍历整个列表
            if j==i:  # 第二遍遍历之后发现了和第一遍遍历相同的元素，比如后面的元素和原始第一个元素相同
                s+=1  #计数器+1
                if s>=2:   # 如果重复出现超过两次
                    dict_key_values_repeat[i]= s  # 将该元素的纪录仅空字典，形成键值对 元素：重复次数

    return dict_key_values_repeat  #循环结束后返回写好数据的字典

if __name__ =='__main__':

    list_given = [random.randint(1,9990999) for i in range(1,1000)]  # 生成列表实例
    print(list_given,'\n**********************')
    print('重复元素：重复次数 如下：\n')
    print(my_counter_function(list_given))
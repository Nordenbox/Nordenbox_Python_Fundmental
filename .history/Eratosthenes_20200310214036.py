import time

scale = int(input('输入你想要的自然数范围: '))  # 输入范围
list_nature = [z for z in range(2, scale + 1)]  # 生成列表
#print('原始列表：', list_nature,'\n--------------')

def get_primes(n, list):   # 一个处理筛选的方法，参数是整除倍数和给定列表
    for i in list:         # 遍历一个列表
        if i % n == 0:     # 当列表中的每一个数字与给定倍数整除无余数的情况下
            list.remove(i) # 去除这个数字
    list.append(n)         # 但是将这个倍数本身在去除之后，重新加回列表之中。
    list.sort(reverse=False) # 将这个列表排序
    return list

time_start = time.time()
for s in list_nature:   # 给定一个列表。注意，是从2 开始的自然数数列。
    get_primes(s, list_nature)  # 这里的参数 s 就是 2，也就是这个数列的第一项。 get_primes 这个函数将使用这个s，作为形参 n 使用。
time_end = time.time()
print('{} 以内Eratosthenes方法筛除之后素数列表为：\n'.format(scale), list_nature)
print('{} 以内素数的个数为 {}, 占比为 {} %.'.
      format(scale, len(list_nature), 100 * ((len(list_nature)) / scale)))
print("计算消耗时间", round(time_end - time_start), "秒")


temp = []
time_start_02 = time.time()
for i in list_nature:
    for skip in range(2, i):
        while i % skip == 0:
            temp.append(i)
            break

final = [item for item in list_nature if item not in set(temp)]
time_end_02 = time.time()
print('----------------------------')
print('使用暴力整除排除方法计算的素数列表： \n',final)
print('{} 以内素数个数为 {}, 占比为 {}%.'.
      format(scale, len(final), 100 * ((len(final)) / scale)))
print("计算消耗时间", round(time_end_02 - time_start_02), "秒")

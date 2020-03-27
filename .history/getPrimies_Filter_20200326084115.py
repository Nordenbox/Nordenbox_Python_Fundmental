''' utf-8'''
import progressbar
import time


def find_primes(n):
    """[使用 Filter 函数筛选质数]

Returns:
    [boolean] -- [false：不是质数。True：是质数]
"""
    p = progressbar.ProgressBar()
    p.start(n)
    if n < 2:
        return False
    else:
        for i in range(2, n):
            p.update(i+1)
            if n % i == 0:
                return False
        else:
            return True
    p.finish()
        # 这个地方很关键，不能在 if 之后接 else，否则需要再写一轮循环。
        # 只需要让 if 语句完全没有 return，进入 for-else，则必然是质数。


get_primes = filter(find_primes, [i for i in range(1, 100001)]) # filter函数，只要满足寻找素数的函数返回值为 False，就在列表中剔除。
a = list(get_primes)
print(a, len(a))
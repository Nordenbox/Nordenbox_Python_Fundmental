""" 这是一个用蒙特卡洛办法计算元圆周率的程序"""

import matplotlib.pyplot as plt
import random
import time
from etaprogress.progress import ProgressBar # 添加可以显示进度条的模块
import sys
# from guppy import hpy  # 查看内存占用的库

x = []  # 两个空列表备用
y = []
t = int(input('throw times: '))  # 选择投掷随机点的次数。最好别超过十亿次，否则 32G 内存会爆掉。
time_start = time.time()
bar = ProgressBar(t, max_width=90)  #设定进度条
for i in range(t):  # for 循环模拟投掷
    m = random.random()  # 每个点的坐标都是 0 到 1 之间的随机小数
    n = random.random()
    if m * m + n * n <= 1:  # 如果这个他们距离远点的距离是小于 1，就添加到一个列表之中。
        x.append(m)
        y.append(n)
        bar.numerator = i #进度条跟随迭代的数字
        print(bar, end='') #打印进度条
        sys.stdout.flush()
    else:
        pass
time_end = time.time()
#h = hpy()
#print(h.heap())  # 查看内存占用
print('落入半圆中的次数：', len(x), '总的投掷次数； ', t)
# plt.scatter(x,y,alpha = 0.62)  #用了符合条件的列表绘制图像。
# plt.title('Pi = {}'.format(4*len(x)/t))  # 圆周率的值等于落入半径为一
# 的圆圈中的点与所有投掷次数的比值的四倍
# plt.show()
print('Pi = {}'.format(4 * len(x) / t))
print('computing time is {} seconds'.format(time_end - time_start))
import numpy
import time


class SquareRoot:

    def __init__(self, n):
        self.n = n

    def root(self):
        for i in range(1, self.n):
            if i * i < self.n < (i + 1) * (i + 1):
                for j in numpy.arange(i, i + 1, 0.001):
                    if j * j >= self.n:  # 这个地方卡了很久，应该是大于，而不是小于。
                        return j


given = SquareRoot(int(input('输入一个数求其平方根： ')))
start = time.time()
print('平方根为： ', format(given.root(), '0.5f'))
end = time.time()
print('耗时为：{:.4}秒'.format(end - start))

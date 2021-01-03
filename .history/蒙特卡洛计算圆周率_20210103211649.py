''' 这是一个用蒙特卡洛办法计算元圆周率的程序'''

import matplotlib.pyplot as plt
import random
x = []
y = []
t = int(input('throw times: '))
for i in range(t):
    m = random.random()
    n = random.random()
    if m*m +n*n <=1:
        x.append(m)
        y.append(n)
    else:
        pass
print(len(x),t)
plt.scatter(x,y,alpha = 0.62)
plt.title('Pi = {}'.format(4*len(x)/t))
plt.show()



import numpy as np
import matplotlib.pyplot as plt
import random
x = []
y = []
s=0
for i in range(10000):
    m = random.random()
    n = random.random()
    if m*m +n*n <=1:
        x.append(m)
        y.append(n)
    else:
        s+=1

plt.scatter(x,y,alpha = 0.62)
plt.title('圆周率为 {:.7}'.format(4*(s+len(x))/len(x)))
plt.show()



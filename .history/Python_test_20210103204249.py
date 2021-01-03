import numpy as np
import matplotlib.pyplot as plt
import random
x = []
y = []
for i in range(100000):
    m = random.random()
    n = random.random()
    if m*m +n*n <=1:
        x.append(m)
        y.append(n)

plt.scatter(x,y,alpha = 0.62)
plt.show()



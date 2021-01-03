import numpy as np
import matplotlib.pyplot as plt
import random
x = []
y = []
for i in range(10000):
    m = random.random()
    n = random.random()
    if m*m +n*n <=1:
        x.append(m)
        y.append(n)

print(x)
print(y)
plt.scatter(x,y,alpha = 0.62)
plt.show()



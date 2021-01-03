import numpy as np
import matplotlib.pyplot as plt
import random
x = []
y = []
n = int(input('throw times: '))
for i in range(n):
    m = random.random()
    n = random.random()
    if m*m +n*n <=1:
        x.append(m)
        y.append(n)
    else:
        pass
print(len(x),n)
plt.scatter(x,y,alpha = 0.62)
plt.title('Pi = {}'.format(4*len(x)/n))
plt.show()



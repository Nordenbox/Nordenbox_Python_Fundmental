import numpy as np
import matplotlib.pyplot as plt
for i in range(10000):
    x = np.random.rand(100)
    y = np.random.rand(100)
    if x*x +y*y ==1:
        plt.scatter(x,y,alpha = 0.62)
        plt.show()



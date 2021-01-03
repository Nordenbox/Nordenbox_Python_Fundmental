import numpy as np
import matplotlib.pyplot as plt
import random

for i in range(10000):
    x = random.random()
    y = random.random()
    if x*x +y*y ==1:
        plt.scatter(x,y,alpha = 0.62)
        plt.show()



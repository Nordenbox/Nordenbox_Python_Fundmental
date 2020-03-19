import matplotlib.pyplot as plt
import numpy as np

from random_walk import *

rw = RandomWalk(9000)
rw.walk_random()
plt.figure(dpi=180, figsize=(10, 4))
plt.plot(rw.x_values, rw.y_values, c='red')
plt.show()

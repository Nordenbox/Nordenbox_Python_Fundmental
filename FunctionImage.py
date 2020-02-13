
import numpy
import matplotlib.pyplot as plt

xlist = []
ylist = []
for items in range(1, 100):
    xlist.append(items)
    y = 1/(items**2)
    ylist.append(y)
plt.plot(xlist, ylist)
plt.show()

import matplotlib.pyplot as plt
import numpy
x = [i for i in numpy.arange(-10.0, 10.0, 0.1)]
y = [t**3 for t in x]
print(x)
print(y)
plt.plot(x, y)
plt.show()

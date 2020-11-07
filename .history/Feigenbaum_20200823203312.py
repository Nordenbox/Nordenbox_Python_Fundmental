import matplotlib.pyplot as plt
import numpy as np

functionDicars_y=[]
functionDicars_i=[]
b = 1.2
i= 0.8
for items in range(1,50):
    y = b*i*(1-i)
    i = b*y*(1-y)

    functionDicars_y.append(y)
    functionDicars_i.append(i)

print(functionDicars_y)
print(functionDicars_i)
plt.plot(functionDicars_y,functionDicars_i)
plt.show()
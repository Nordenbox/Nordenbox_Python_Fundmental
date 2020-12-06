import time
import pandas as pd

size_of_vector = 10000001
x = range(size_of_vector)
y = range(size_of_vector)
t1 = time.time()


'''
z = []
for i in range(len(x)):
    z.append(x[i]+y[i])

print(time.time()-t1)
'''
z= pd.Series(x)+pd.Series(y)
t2= time.time()-t1
print(z)
print(t2)
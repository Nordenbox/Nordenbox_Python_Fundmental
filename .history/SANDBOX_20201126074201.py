import time

size_of_vector = 1000001
x = range(size_of_vector)
y = range(size_of_vector)
t1 = time.time()
z = []

for i in range(len(x)):
    z.append(x(i)+y(i))

print(time.time()-t1)
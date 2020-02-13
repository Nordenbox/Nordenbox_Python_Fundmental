import math
a = 0
sum = 0

while a <= 10000:
    a = a + 1
    sum = sum + (6/(a**2)) # 欧拉公式
    
print (math.sqrt(sum))
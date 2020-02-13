'''
k=0
n=1
z=0
s=0
for n in range(1,1000000):
    z += 1/n # 调和级数求和
    k += ((-1*1)**(n+1))/(n) # 另外一种正负号交替
    s += 1/(n**2)
print ("调和级数=",z,"正负交替调和=",k,"平方数倒数相加=",s)
'''

import sys
for i in sys.path:
    print(i)
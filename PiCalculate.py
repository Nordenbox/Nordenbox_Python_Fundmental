
n=0
k=0
num = input('input a number(10 **) that caculate using Lebniz Formula : ')
num = int(num)
for n in range(pow(10,num)):
    
    k += ((-1)**n)/((2*n)+1) # 莱布尼茨公式表达式
    print(k*4)
print ("莱布尼茨公式推导圆周率为",k*4)

k=1
n=1


for n in range(1,pow(10,num)):
    
    k = k * ((n*2)/(2*n-1))*((2*n)/(2*n+1)) # 沃利斯公式
    
print ("沃利斯公式推导圆周率为",k*2)
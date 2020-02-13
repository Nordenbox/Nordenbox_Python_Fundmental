n=0
k=0
num = input('input a number that caculate using Lebniz Formula : ')
num = int(num)
for n in range(num):
    
    k += ((-1)**n)/((2*n)+1) # 莱布尼茨公式表达式
    
print ("莱布尼茨公式推导圆周率为",k*4)

k=1
n=1
num2= input('input another number that caculate using Wallis Formula: ')
num2=int(num2)
for n in range(1,num2):
    
    k = k * ((n*2)/(2*n-1))*((2*n)/(2*n+1)) # 沃利斯公式
    
print ("沃利斯公式推导圆周率为",k*2)
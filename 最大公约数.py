
def gcdRecur(a,b):
    if a>b:
        a,b=b,a
    for i in range(a,1,-1): # 如果是最小公约数就是正序，最大为逆序
        if a%i ==0 and b%i ==0:
            return i
        
s= gcdRecur(100,80)
print(s)
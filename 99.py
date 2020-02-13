import time
h = 0
#v=0
while h < 9:
    h=h+1
    v = 0
    while v < 9:
        v=v+1
        
        print('%d*%d=%d '%(h,v,h*v),end='')
        time.sleep(0.1)
    print()
print('-----------------')
for i in range(1,10):
    for j in range(1,10):
        print('%dX%d=%d '%(i,j,i*j),end='')
    print()
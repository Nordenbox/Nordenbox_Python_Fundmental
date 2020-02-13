while True:
    n=1
    x=input('Enter a number')
    y=0
    if x == 0:
        continue
    try:
        y=int(x)
    except:
        pass
    for i in range(1,y+1):
        n = n*i
    print(n)

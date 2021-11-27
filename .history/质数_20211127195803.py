prime = []
for a in range(2,101):
    d = 0
    
    for b in range(2, a-1):
        if a % b == 0:
            
            pass
        else:
            
            #print(a)
            prime.append(a)
print(prime)
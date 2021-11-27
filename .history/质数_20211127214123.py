primenumbers = []

for i in range(2, 100):
    j=2
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        primenumbers.append(i)
print(primenumbers)
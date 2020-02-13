import sys
def collatz(number):
    print(number)
    if number == 1:
        sys.exit()
    elif number % 2 == 1 :
        t=number*3+1
        collatz(t)
    else:
        t=number//2
        collatz(t)

if __name__=='__main__':
    n=input('Enter number: ')
    n=int(n)
    collatz(n)



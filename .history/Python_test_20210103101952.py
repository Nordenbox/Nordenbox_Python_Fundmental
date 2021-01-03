
class SquareRoot:

    def __init__(self, n):
        self.n = n

    def root(self):
        for i in range(self.n+1):
            if i**i < self.n:
                for j in range(i,i+1, 0.01):
                    while j**j<+self.n:
                        print(j)
                    else:
                        continue

given = SquareRoot(int(input('input a int : ')))
given.root()

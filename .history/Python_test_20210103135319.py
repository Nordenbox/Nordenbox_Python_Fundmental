import numpy

class SquareRoot:

    def __init__(self, n):
        self.n = n

    def root(self):
        for i in range(1, self.n):
            if i * i < self.n < (i + 1) * (i + 1):
                print(i)
                for j in numpy.arange(i, i + 1, 0.001):
                    if j * j < self.n:
                        print(j)


given = SquareRoot(int(input('input a int : ')))
given.root()

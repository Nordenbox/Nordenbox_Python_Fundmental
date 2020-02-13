
class FibMethods():
    """三种生成斐波拉契数列的方法."""

    def fib_recursive(self, m):

        if m <= 0:
            return 1
        elif m == 1:
            return 1
        else:
            return self.fib_recursive(m-1)+self.fib_recursive(m-2)

    def fib_loop(self):

        n1 = 0
        n2 = 1
        fib = []
        for i in range(1, m):

            n_next = n1 + n2
            fib.append(n_next)
            n1 = n2
            n2 = n_next
        print(fib)

    def fib_yield(self):
        a, b = 0, 1
        n = []
        for i in range(m):

            a, b = b, a+b
            n.append(a)

        print(n)


instance_test = FibMethods()
m = int(input('需要生成多少项斐波拉契数列：'))
choose = int(input('使用哪一种斐波拉契生成方法？\n 1，迭代方法、\n 2，循环方法 \n 3，交换赋值方法 \n'))
if choose == 1:
    instance_test.fib_recursive(m)
    for i in range(m):
        print(instance_test.fib_recursive(i), end=',')
elif choose == 2:
    instance_test.fib_loop()
else:
    instance_test.fib_yield()

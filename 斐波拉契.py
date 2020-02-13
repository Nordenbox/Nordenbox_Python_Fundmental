import time


class FibMethods():
    """三种生成斐波拉契数列的方法."""

    def fib_recursive(self, m):    # 在类中的函数如果要调用自己，需要用到 self。这和静态函数并不一致。

        if m <= 0:
            return 1
        elif m == 1:
            return 1
        else:
            # 函数调用自身，需要有 self 做实例对象。参数如果小于零则调用条件判断。
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


instance_test = FibMethods()    # 实例化
m = int(input('需要生成多少项斐波拉契数列：'))
choose = int(input('使用哪一种斐波拉契生成方法？\n 1，迭代方法、\n 2，循环方法 \n 3，交换赋值方法 \n'))
if choose == 1:
    instance_test.fib_recursive(m)    # 给予一个实例，并且有参数 m，该实例调用函数。
    for i in range(m):
        # 这个实例可以直接调用函数 fib_recursive。
        print(instance_test.fib_recursive(i), end=',')
elif choose == 2:
    instance_test.fib_loop()
else:
    instance_test.fib_yield()

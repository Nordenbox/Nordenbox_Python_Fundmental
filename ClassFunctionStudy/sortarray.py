import random

''' argument 'arr' MEANS a List by given in Python'''


class SortRandomList:    # 一个类，包裹了一些方法。

    def find_smallest_one(self, arr):   # 形式参数arr就是一个等待被给定的列表。
        smallest = arr[0]     # 将这个列表的第一个元素赋值给这个 smallest 变量，我们先假定这个元素最小。
        smallest_index = 0    # 最小元素的索引值被初始化为零。以后会被替换。
        for i in range(1, len(arr)):    # len(arr)是列表的长度，i 将用这个数字来累进。
            if arr[i] < smallest:    # 从第二个元素（i的值是 1 ）开始，比较每一个元素和第一个元素的大小。因为之前我们已经将第一个元素给予了一个变量 smallest。
                # 如果小于第一个元素（index = 0），就将这个元素重新赋值给smallset，将其定义为最小的元素。然后不断循环这一过程。
                smallest = arr[i]
                smallest_index = i    # 并且将此时的 i 定义为这个最小元素的索引值，实际上在重新排序之前，我们仅仅知道这个最小元素的索引值即可。
        return smallest_index    # 这个函数输出的仅仅是最小元素的索引值。但这很有用。

    def selectionSort(self, arr):    # 给定一个列表，然后对其进行排序操作。
        newArr = []
        for i in range(len(arr)):
            # 调用 find_smallest_one 函数，使用其返回的最小索引值，将这个列表的最小值的索引给予变量 smallest。
            smallest = self.find_smallest_one(arr)
            newArr.append(arr.pop(smallest))

            ''' 将最小值的索引，作为一个参数，在给定的列表中去除最小的那个元素，将其添加给新空列表。往复循环，这一行有点费解，需要仔细思考。
            要理解这一点，需要考虑到，pop 函数返回的是被删除的元素，而不是原先列表留下来的元素。这一点和 delet 不一样。del 命令返回的是被修改过的列表。
            所以 apeend 添加的其实就是被拿走的最小值本身。所以取名 pop（挤压出） 是有道理的。'''

        return newArr    # 返回一个排列好的列表。

    def randomList(self, arr):    # 定义一个生成乱序列表的方法。
        randomList = []    # 给予一个空列表
        lenth = int(input('输入一个数字表示你需要多大的列表: '))    # 要求输入即将生成列表的长度（元素个数）。
        # 要求输入即将生成列表的随机数乱序跨度，从 1 开始。
        large = int(input('输入一个数字表示在多大范围内随机生成元素: '))
        for i in range(1, lenth):    # 遍历这个新列表的个数。
            issue = random.randint(1, large)    # 将 1 到跨度之间生成随机数给予变量 issue。
            randomList.append(issue)    # 将每一个生成的乱序随机数添加到空列表 randomlist 中。
        return randomList


s = SortRandomList()    # 将类赋值给变量备用，实际就是实例化。
comtemp_list = []    # 建立一个空列表备用。
random_list_made = s.randomList(comtemp_list)    # 实例调用函数（方法）建立一个随机乱序列表。
print('这就是你想要的随机列表： \n\n', random_list_made, '\n')    # 打印这个随机乱序列表。
smallestOne = s.find_smallest_one(random_list_made)    # 找到列表中的最小值，调用函数find_smallest_one，给予刚才建构的乱序列表做参数。
print('这个列表的最小值是： \n\n', random_list_made[smallestOne], '\n')    # 打印这个最小值。
sortedlist = s.selectionSort(random_list_made)    # 将这个乱序列表排序，调用类中的排序函数。
print('排序之后的列表是 : \n\n', sortedlist, '\n')

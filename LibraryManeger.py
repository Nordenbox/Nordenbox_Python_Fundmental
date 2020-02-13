class Book_DataInitial:     #初始化书籍的基本信息，数据结构，参数的构成和借出状态的定义。
     
    def __init__(self, name, author, comment, state = 0):  #自动运行的初始化函数，给予书籍的基本参数，这些参数决定了书籍的属性。 最后一个参数state给出数值，实际上就是默认。
        self.name = name  # 名称属性。将未来会确定的书名参数赋值给 init 初始化函数中的的实例。
        self.author = author # 作者属性。函数内部的指令和程序，将作者参数给予一个实例化的属性。
        self.comment = comment #书评参数赋值给一个实例。
        self.state = state #状态参数。这个参数很重要，虽然在定义函数的时候，这个值是零，但以后有可能变化。这个零的值，显然是初始化。
        # 初始化函数的重要，既然注定要运行，就做一些初始化的事情，比如给予最重要的参数。在后面用 Book_DataInitial 赋值给实例的实例（实例化）
        # 的时候，可以将参数歘递给实例。

    def __str__(self):  
        ''' state 可以被定义为零，也可以是 1，但是无法直接输出给用户 0 或者 1，用户要看的是借出，或者没借出。所以需要转换。''' 
        status = '未借出' # 默认就是没借出。在初始化函数里就是。
        if self.state == 1:  # 做转换。
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status) # 这里的 status 不是参数，而是一个变量。
        # 返回值给予 __str()__ 若执行这个函数，就可以得到一个字符串，这个字符串输出书的状态。
 
class BookManager: 

    books = [] # 这是一个列表。这个列表的目的在于生成一个数据库。之所以出现在这里，是因为这个列表被主要的函数管理功能所运用。
    def __init__(self): # 初始化一些书籍的数据，每次启动管理系统的时候都会加载这个函数。读取书籍库中的数据。
        book1 = Book_DataInitial('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。') #默认参数 state=0
        book2 = Book_DataInitial('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book_DataInitial('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。',1)# 这个地方有参数 state
        # 将类 Book_DataInitial 赋值给予列表序列，可以看出前面对 Book_DataInitial 类的定义的重要性。就是该类不能是数据本身，而是对数据的一种范式规定。
        # 比如数据的参数有哪些？借出还是没有借出是怎么定义的。
        self.books.append(book1) # 将每一行添加的书籍信息，加入列表 books。
        self.books.append(book2)
        self.books.append(book3)
  
    def menuUI(self): # 主功能函数。她调用其他函数。在我看来，函数之间不能互相调用，否则会乱。
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True: # 无限循环。这种情况一般用于要求用户反复操作的情况下。也就是程序要一直运行。
            print('-')
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：')) # 切换各种功能函数，执行不同的功能。
            if choice == 1:
                self.show_all_book() # self 指代这个函数本身作为一个实例， 自身使用和运行这里给出的函数 show_all_book
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5: # 直到用户选择此项，该程序才停止运行。这是一种模板。
                print('感谢使用！愿你我成为爱书之人，在茫茫书海中相遇。')
                break
 
    def show_all_book(self): # 显示所有书籍的函数
        for items in self.books: # 这里的 self 指代这个函数本身，作为一个实例使用和运行列表 books。定义一个变量 items 来遍历这个列表。
            print(items) # 这个 books 列表是一个复合列表，即每一个列表元素都包含子元素，所以用 items 这个变量可以实现分行打印出来，显得容易观看。
            print('') 

    def add_book(self): # 添加书籍函数
        new_name = input('请输入书籍名称：') # 定义若干变量，然后将这些变量作为参数，给予书籍。
        new_author =  input('请输入作者名称：') # 定义若干变量，然后将这些变量作为参数，给予书籍。
        new_comment = input('请输入书籍推荐语：') # 定义若干变量，然后将这些变量作为参数，给予书籍。
        new_book = Book_DataInitial(new_name, new_author, new_comment) 
        # 这些参数替换原有类 Book_DataInitial 的参数，成为新书的参数。 这个里没有给出参数 state，就是默认所有新书的 state 参数为默认 state = 0.就是没有借出。
        # 这就能看出来原来的参数 state = 0 的妙处了。如果不在那里预先定义，实际上每次都要确认。
        self.books.append(new_book)# 自身调用列表添加。
        print('书籍录入成功！\n')

    def check_book(self,name): # 这个函数主要为后面两个模块服务。参数 name 的作用在于书名的替代物。后续会被别的函数给与输入。
        for items in self.books:  # books这个列表在所有函数之前就被定义好了，可见一斑。这个地方是要用的。
            if items.name == name: #比较输入的书名与 books 列表里面的书名，如果相同，就返回原来的书名。items.name 在这里的意思是books 列表中的 name。
                 return items 
        else:
            return None # 如果书名不相同，返回另外一个值，比如空值。

    def lend_book(self): # 借书模块。
        name = input('请输入借阅书籍的名称：') # 需要用户输入一个字符串，给予变量 name。
        res = self.check_book(name) # 这个变量将替换之前 check_book 函数中的参数name。并且和 items.book 做比较。返回值是 items 或者 none

        if res != None: # res 不等于none，也就是说，书名是有的。是借出或者没有借出的状态。
            if res.state == 1: # 被解除的状态。这里的 res.state 来自于初始函数中的参数 state，而这个初始函数的 state 来自于继承的父类。
                print('你来晚了一步，这本书已经被借走了噢\n')
            else:
                print('借阅成功，借了不看会变胖噢～')
                res.state = 1 # 如果原有不等于 1，也就是现在可以借出，就将书变成 1，也就是借出状态。这个函数是借书函数，默认你肯定要借走。
        else:
            print('这本书暂时没有收录在系统里呢') # 等于 none，表示没有这本书。

    def return_book(self):
        name = input('请输入归还书籍的名称：')
        res = self.check_book(name)
        # 调用check_book方法，将返回值赋值给变量res
        if res == None:
        # 如果返回的是空值，即这本书的书名不在系统里
            print('没有这本书噢，你恐怕输错了书名～\n')
        else:
        # 如果返回的是实例对象
            if res.state == 0: 
             # 如果实例属性state等于0，即这本书的借阅状态为'未借出'
                print('这本书没有被借走，在等待有缘人的垂青呢！')
            else:
             # 如果实例属性state等于1，即状态为'已借出'
                print('归还成功！')
                res.state = 0
      

manager = BookManager() # 将BookManager这个类赋值给 manager这个实例
manager.menuUI() #实例调用函数 menuUI（）

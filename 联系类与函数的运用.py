class Cart:
    '''Cart shoping ''' # 一个购物的类
    
    # 初始化一个字典，即购物车。里面是物品和单价
    def __init__(self,itemDict):
        self.itemDict = itemDict
       
    # 计价函数。即遍历字典，然后通过键来取值   
    def getPrice(self,itemDict):
        result = 0
        for i in self.itemDict:  # 遍历这个字典，实质是取键。
            result = itemDict[i] +result    # 键就对应着键值
        print(result)    
            
        
    def deleteItem(self,deleteItem):    # 删除一个给定的商品，参数就是商品名字
        del self.itemDict[deleteItem]
    
    def addItem(self,addItem,price_eache): # 添加一个商品，参数为商品的名字和单价
        self.itemDict[addItem]=price_eache
    
itemDict = {"glass": 600, "phone": 6000}

ming = Cart(itemDict)   # 小明调用这个类
ming.deleteItem("glass")
ming.addItem('milk',70)
ming.getPrice(itemDict)
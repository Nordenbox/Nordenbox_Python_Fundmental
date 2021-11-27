price = {"牛奶":5, "面包":4.5, "可乐":6, "饼干":7, "糖果":2.5, "苹果":5.5}
num = {"牛奶":3, "面包":5, "可乐":7, "饼干":3, "糖果":5, "苹果":4}

def sum(price,num):
    
    count =0
    for i in price.keys():
        count = count+ price[i]*num[i]
    print(f"您购买的商品总价为{count}元！")

sum(price,num)
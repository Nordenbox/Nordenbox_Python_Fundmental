
import random



dishs = ['宫保肉丁','西湖醋鱼',' 711 套餐','肯德基全家桶','鳗鱼盖饭']
restaurents = ['吉野家','烤肉季','小四川','隆德餐厅','社交咖啡店']
    
    
choose = int(input('为甚不知道吃什么: \n1, 完全不知道吃什么\n2, 餐厅选择困难\n'))

if choose == 1:
    
    while True:
        print('---------------')
        print('给你一个选择: '+random.choice(dishs))
        decide = input('喜欢吗? Y or N.请选择。')
        if decide !='N':
            break
        else:
            continue
    
else:
    
    while True:
        print('---------------')
        print('给你一个选择: '+random.choice(restaurents))
        
        decide = input('喜欢吗? Y or N.请选择。')
        if decide !='N':
            break
        else:
            continue




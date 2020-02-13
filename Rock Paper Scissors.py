
while True:
    
    
    try:
        print('\n欢迎使用除法计算器！\n')
        x = input('请你输入被除数：')
        y = input('请你输入除数：')
        z = float(x)/float(y)
        print(x,'/',y,'=',z)
        break 
        
    except ZeroDivisionError:
        print('零不能作除数')
    except ValueError:
        print('不能输入字符')

    # 下面是 print函数的一种用法，用逗号隔开，可在同一行打印不同类型的数据。
     # 当成功运行一次除法运算后，退出程序。1
print('##########  九九乘法口诀  ############')
for i in range(1,10):
    for y in range(1,10):
        print(i,'x',y,'=',i*y,end=' | ')
        while y==9:
            print('\n-------------------------')
            break
print('Ada 会乘法口诀啦！！！！！！ ：）')
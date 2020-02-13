mind = 24
guest = int(input('speak your number: \n'))
while guest != mind:
    
    
    guest = int(input(' one more again: \n'))
    if guest > 24 :
        print('it is too high')
        continue
    elif guest< 24:
        print('it is too small')
        continue
    else:
        pass
else:
    print('Bingo')  
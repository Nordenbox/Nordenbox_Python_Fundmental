def rev(s):
    temp = ''
    if s == "" or len(s) == 1:
        print('do not need')
    else:
        for i in s:
            temp = i + temp
    print(temp)


rev("123456789")


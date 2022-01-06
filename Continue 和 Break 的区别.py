for letter in '123A56':
    if letter == 'A':
        #continue  #此处跳出for枚举'A'的那一次循环，其他继续
        break   # 直接从 A 处停止，不在执行本次循环，执行下一行
    print('当前字母 :', letter)
'''
continue 输出：  
当前字母 : 1
当前字母 : 2
当前字母 : 3
当前字母 : 5
当前字母 : 6

'''
'''
Break 输出：
当前字母 : 1
当前字母 : 2
当前字母 : 3
'''
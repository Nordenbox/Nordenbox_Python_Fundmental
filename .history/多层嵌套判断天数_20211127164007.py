d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# 一个月份与天数的字典。


def calDay(year, month, day):
    # 按照闰年费闰年，设定两个字典。
    dRun = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    dNotRun = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    count = 0

    if year not in range(1000, 9999): # 判断年的输入合法性。
        print('year wrong')

    else:

        if month not in range(1, 12): # 月的合法性
            print('month wrong')
        else:

            if day > 30 and month in [2, 4, 6, 9, 11]: # 大小月的合法性
                print('day wrong')
            else:

                if year % 4 == 0: # 闰年与否
                    for i in range(1, month): # 多少月，就有多少循环次数
                        count = count + dRun[i] + day # 在相对的字典中寻找与月相对应的键值：天数
                    print(count)
                else:
                    for i in range(1, month):
                        count = count + dNotRun[i] + day
                print(count)


calDay(2021, 5, 20)
d = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def calDay(year, month, day):
    dRun = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    dNotRun = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    count = 0

    if year not in range(1000, 9999):
        print('year wrong')

    else:

        if month not in range(1, 12):
            print('month wrong')
        else:

            if day > 30 and month in [2, 4, 6, 9, 11]:
                print('day wrong')
            else:

                if year % 4 == 0:
                    for i in range(1, month):
                        count = count + dRun[i]

                    return  count+day

                else:
                    for i in range(1, month):
                        count = count + dNotRun[i]
                    return count + day


result = calDay(2021, 5, 20)
print(f"2021年5月20日是这一年的第{result}天！")

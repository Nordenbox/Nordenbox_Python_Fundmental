
temp = input("输入年份:")
YEAR = int(temp)
if (YEAR % 4 == 0 and YEAR % 100 != 0) or (YEAR % 400 == 0 and YEAR % 3200 != 0) or YEAR % 172800 == 0:    
    print ("闰年")
else:
    print ("非闰年")
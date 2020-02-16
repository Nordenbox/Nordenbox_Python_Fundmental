import random
import time
import os
import subprocess


howmuch = int(input("你想做几道题，输入一个数字："))


corrected = 0
wrong = 0
counting = howmuch
sum_wrong_list = []
minos_wrong_list = []
sum = 0
minos = 0

mathHouse = [random.randint(1, 20) for i in range(howmuch)]
print(mathHouse)
time_start = time.time()
print("--------------\n 开始计时……")

for items in mathHouse:

    plus = random.randint(1, 20)
    p = random.randint(0, 1)
    if p == 1:
        sum = int(input("%d+%d= " % (items, plus)))
        if sum == items + plus:
            corrected = corrected + 1
        else:
            sum_wrong_list.append("%d+%d= %d" % (items, plus, sum))
            wrong = wrong + 1

    else:
        if items < plus:
            minos = int(input('%d-%d= '%(plus, items)))
            if minos == plus - items:
                corrected = corrected + 1
            else:
                minos_wrong_list.append("%d-%d=%d " % (plus, items, minos))
                wrong = wrong + 1
        else:
            minos = int(input("%d-%d= " % (items, plus)))
            if minos == items - plus:
                corrected = corrected + 1
            else:
                minos_wrong_list.append("%d-%d=%d " % (items, plus, minos))
                wrong = wrong + 1

    counting = counting - 1
    print("\t还剩下%d 道题。" % counting)

subprocess.call(["afplay", '/Users/nordenbox/Downloads/win31.mp3'])
print("正确为%d，错误为%d。" % (corrected, wrong), "你的分数是%d分" % (corrected / howmuch * 100))
print("错误的题目是：\n", sum_wrong_list, "\n", minos_wrong_list)

time_end = time.time()
print("消耗时间", round(time_end - time_start), "秒")
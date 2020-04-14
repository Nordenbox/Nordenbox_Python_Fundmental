import random
import time
import os
import subprocess


def mode_choice():
    print('请选用练习模式：\n1，选择练习题目数.')
    print('2, 选择练习时间')
    choice_num = int(input('您的选择： '))
    if choice_num == 1:
        practicese_times = int(input('您要做几道题： '))

        practice_multipile(practicese_times)
    else:
        multipile_time()





def multipile_time():
    pass


def practice_multipile(times):
    corrected = 0
    wrong = 0
    counting = times
    sum_wrong_list = []
    minos_wrong_list = []
    sum = 0
    minos = 0

    mathHouse = [random.randint(1, 20) for i in range(times)]
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
                minos = int(input("%d-%d= " % (plus, items)))
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

    subprocess.call(["afplay", "/Users/nordenbox/Documents/GitHub/NordenboxPython/Nordenbox_Python_Fundmental/media/wfw311.mp3"])
    print("正确为%d，错误为%d。" % (corrected, wrong), "你的分数是%d分" % (corrected / times * 100))
    if sum_wrong_list != [] and minos_wrong_list != []:
        print("错误的题目是：\n", sum_wrong_list, "\n", minos_wrong_list)
    elif sum_wrong_list == [] and minos_wrong_list != []:
        print("错误的题目是：\n", minos_wrong_list)
    elif sum_wrong_list != [] and minos_wrong_list == []:
        print("错误的题目是：\n", sum_wrong_list)

    time_end = time.time()
    print("消耗时间", round(time_end - time_start), "秒")


mode_choice()


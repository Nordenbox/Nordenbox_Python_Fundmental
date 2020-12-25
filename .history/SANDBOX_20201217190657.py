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
        duration = float(input('请输入做题时间（分钟）： '))
        practice_timelimit(duration)





def practice_timelimit(duration):

    time_start = time.time()
    print("--------------\n 开始计时……")
    count= 0
    corrected = 0
    wrong = 0
    sum_wrong_list = []
    minos_wrong_list = []
    sum = 0
    minos = 0
    while True:



        multipy = random.randint(1, 10)
        multipied=random.randint(1, 10)
        p = random.randint(0, 1)

        sum = int(input("%d*%d= " % (multipy, multipied)))
        if sum == multipy * multipied:
            corrected = corrected + 1
        else:
            sum_wrong_list.append("%d*%d= %d" % (multipy, multipied, sum))
            wrong = wrong + 1


        time_now = time.time()
        time_timelapse = time_now - time_start
        time_remain = duration*60 - time_timelapse
        count += 1
        print('您的剩余时间为{}秒。已做了{}题。'.format(round(time_remain,1), count))


        if time_remain<=0:
            print('您已经超时{}秒'.format(abs(round(time_remain,1))))
            break


    subprocess.call(["afplay", "/Users/nordenbox/Documents/GitHub/NordenboxPython/Nordenbox_Python_Fundmental/media/wfw311.mp3"])

    print("正确为%d，错误为%d。" % (corrected, wrong), "你的分数是%d分" % (corrected / count * 100))
    if sum_wrong_list != [] :
        print("错误的题目是：\n", sum_wrong_list, "\n", minos_wrong_list)
    else:
        print('全对了！！！！')

    time_end = time.time()




def practice_multipile(times):
    corrected = 0
    wrong = 0
    counting = times
    sum_wrong_list = []
    minos_wrong_list = []
    sum = 0
    minos = 0

    mathHouse = [random.randint(1, 10) for i in range(times)]
    time_start = time.time()
    print("--------------\n 开始计时……")

    for multipied in mathHouse:

        multipy = random.randint(1, 10)

        sum = int(input("%d*%d= " % (multipy, multipied)))
        if sum == multipied * multipy:
            corrected = corrected + 1
        else:
            sum_wrong_list.append("%d*%d= %d" % (multipy, multipied, sum))
            wrong = wrong + 1


        counting = counting - 1
        print("\t还剩下%d 道题。" % counting)

    subprocess.call(["afplay", "/Users/nordenbox/Documents/GitHub/NordenboxPython/Nordenbox_Python_Fundmental/media/wfw311.mp3"])
    print("正确为%d，错误为%d。" % (corrected, wrong), "你的分数是%d分" % (corrected / count * 100))
    if sum_wrong_list != [] :
        print("错误的题目是：\n", sum_wrong_list, "\n", minos_wrong_list)
    else:
        print('全对了！！！！')

    time_end = time.time()

    time_end = time.time()
    print("消耗时间", round(time_end - time_start), "秒")


mode_choice()

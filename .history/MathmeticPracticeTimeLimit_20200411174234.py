import random
import time
import os
import subprocess


def mode_choice():
    print('请选用练习模式：\n1，选择练习题目数。\n')
    print('2, 选择练习时间')
    choice_num = int(input('您的选择： '))
    if choice_num == 1:
        multipile_issues()
    else:
        multipile_time()


def multipile_issues():
    practicese_times = int(input('您要做几道题： '))
    for i in range(practicese_times):
        practicese_issues()

    print("正确为%d，错误为%d。" % (practicese_issues.corrected, practicese_issues.wrong),
          "你的分数是%d分" % (practicese_issues.corrected / practicese_times * 100))
    if practicese_issues.sum_wrong_list != [] and practicese_issues.minos_wrong_list != []:
        print("错误的题目是：\n", practicese_issues.sum_wrong_list,
              "\n", practicese_issues.minos_wrong_list)
    elif practicese_issues.sum_wrong_list == [] and practicese_issues.minos_wrong_list != []:
        print("错误的题目是：\n", practicese_issues.minos_wrong_list)
    elif practicese_issues.sum_wrong_list != [] and practicese_issues.minos_wrong_list == []:
        print("错误的题目是：\n", practicese_issues.sum_wrong_list)


def multipile_time():
    pass


def practicese_issues():
    orrected = 0
    wrong = 0
    #counting = howmuch
    sum_wrong_list = []
    minos_wrong_list = []
    sum = 0
    minos = 0

    while True:

        plused = random.randint(1, 20)
        plus = random.randint(1, 20)
        p = random.randint(0, 1)
        if p == 1:
            sum = int(input("%d+%d= " % (plused, plus)))
            if sum == plused + plus:
                corrected = corrected + 1
            else:
                sum_wrong_list.append("%d+%d= %d" % (plused, plus, sum))
                wrong = wrong + 1

        else:
            if plused < plus:
                minos = int(input("%d-%d= " % (plus, plused)))
                if minos == plus - plused:
                    corrected = corrected + 1
                else:
                    minos_wrong_list.append(
                        "%d-%d=%d " % (plus, plused, minos))
                    wrong = wrong + 1
            else:
                minos = int(input("%d-%d= " % (plused, plus)))
                if minos == plused - plus:
                    corrected = corrected + 1
                else:
                    minos_wrong_list.append(
                        "%d-%d=%d " % (plused, plus, minos))
                    wrong = wrong + 1

        return corrected, wrong, sum_wrong_list, minos_wrong_list


mode_choice()


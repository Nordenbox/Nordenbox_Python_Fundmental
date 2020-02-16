""" This is a progame for practice litsen and spell for my daughter"""

import os
import random
import subprocess


file_path = (
    r"/Users/nordenbox/PycharmProjects/StudyProject/Speech_US"
)  # read mp3 files from my file folder to ready pronunce
file_list = []  # build a empty list to standby
for i in os.listdir(
    file_path
):  # using os module to traverse the mp3 files in the certain path
    file_list.append(os.path.join(file_path, i))  # creat a list of multipile mp3 paths
random.shuffle(file_list)  # randoms the orders of list for repeatively use
print("---------\n我们开始吧！\n--------------")
print("########### LITSEN & SPELL #############")

for items in file_list:  # traverse the list that randomed order, items = specific path name

    subprocess.call(["afplay", items])  # for each files recalls os subprocess module to apply afplay to play mp3 files
    A = True  # set the condition of While loop
    while A:  # if condition is True loop runs

        wait_word = input("输入听到的单词：\n")  # variables as inputed words
        if wait_word != os.path.basename(os.path.splitext(items)[0]):  
            # if word inputed not equal to the specific file name( by using os module function to obtain basename)
            print("no!!! 再来一遍！")
            subprocess.call(["afplay", items])  # sounds again
        else:
            print("Yes! 下一个")
            A = False  # jump out of loop
print("-----------\nOK! We Finished\n-------------")

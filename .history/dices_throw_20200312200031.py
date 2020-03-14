import random


def roll_dice(total=5):
    rolls = []
    for i in range(0, total):
        rolls.append(random.choice(range(1, 7)))
    return rolls


def roll_once():
    total_dice = []
    for i in range(0, 4):
        total_dice.append(roll_dice(20000))
    record = {}
    index = 0
    #print(total_dice)

    for i in total_dice[0]: # 遍历第一个子列表
        def find():
            for j in total_dice[1:]:
                if j[index] != i:
                    break
            else:
                record[index] = i
        find()
        index += 1
    print(len(record), record)

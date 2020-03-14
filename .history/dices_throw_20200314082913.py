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
    print(total_dice)

    for each_dice in total_dice[0]: # 遍历总列表中的第一个子列表，然后后面的列表一一对照
        def find():
            '''遍历第二个子列表，如果不相等就跳出，如果相等就继续增加一个键值对，第二个子列表循环结束,跳出函数'''
            for j in total_dice[1:]:  # 遍历总列表的第二个子列表开始的后续，直到最后一个子列表
                if j[index] != each_dice:   # 如果第二子列表的第一个元素和第一个子列表中的元素不相等。
                    break    # 跳出循环。
            else:                           # 第二子列表的第一个元素和第一个子列表中的元素不相等。
                record[index] = each_dice    # 字典 record 增添一个键值对
        find()
        index += 1
    print(len(record), record)



roll_once()

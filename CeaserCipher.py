""" 一个凯撒密码的简单加密程序。给定一个句子，会按照加密方式加密，输出密文。"""


my_alphabeta = "abcdefghijklmnopqrstuvwxyz"  # 自己定义一个字母表顺序表，不适用 ascii 码

oringnal = text = input("input a sentencen 输入凯撒需要的明文：").lower()  # 输入明文,并且改成小写字母。
encoding_shift = int(input("input the encoding shift\n输入字符偏移量："))
newtext = ""    # 建立一个空的字符串

for s in range(0, len(text)):  # 变量s遍历每一个字符，长度为句子的长度，标点符号不算。
    # print(len(text))
    # print(text[s])
    if text[s] == " ":  # 遍历的字符遇到空格的情况，将空格保持不变。
        newtext = newtext + " "
    elif text[s] == ',':    # 遍历的字符遇到逗号的情况，将保持不变。
        newtext = newtext + ','
    elif text[s] == '.':    # # 遍历的字符遇到句号的情况，将保持不变。
        newtext = newtext +'.'
    else:    # 排除了以上情况之后 ……
        num = my_alphabeta.index(text[s]) + encoding_shift
        """ 将目前遍历到的字符s，检查其在我设定的字母顺序表的索引值，然后加上偏移量.
        给出一个新的索引值。给予变量 num。"""
        if num >= 25:
            num = num - 26  # 如果出现了偏移值超过了 26 个字母的长度，就循环到下一轮.
        else:
            num = num
        newtext = newtext + my_alphabeta[num]    # 空的字符串直接给予偏量计算后的字母


print("Finally Ceaser saw this 最终凯撒看到的是:")
print("原始明文：", oringnal)
print("加密密文：", newtext)
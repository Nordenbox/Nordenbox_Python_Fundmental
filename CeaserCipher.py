""" 一个凯撒密码的简单加密程序。给定一个句子，会按照加密方式加密，输出密文。"""

my_alphabeta = "abcdefghijklmnopqrstuvwxyz"  # 自己定义一个字母表顺序表，不适用 ascii 码

oringnal = text = input("input a sentencen 输入凯撒需要的明文：")  # 输入明文
encoding_shift = int(input("input the encoding shift\n输入字符偏移量："))


for s in range(0, len(text)):  # 变量s遍历每一个字符，长度为句子的长度，不包含标点符号。
    # print(len(text))
    # print(text[s])
    if text[s] == " ":  # 遍历的字符遇到空格的情况，将空格保持不变。
        text = text.replace(text[s], " ", 1)
    else:
        num = my_alphabeta.index(text[s]) + encoding_shift
        """ 将目前遍历到的字符s，检查其在我设定的字母顺序表的索引值，然后加上偏移量.
        给出一个新的索引值。给予变量 num。"""
        if num >= 25:
            num = num - 26  # 如果出现了偏移值超过了 26 个字母的长度，就循环到下一轮.
        else:
            num = num
        text = text.replace(text[s], my_alphabeta[num], 1)
    """将原来的明文里面的相对应的字符，在遍历到的情况下，被替换为我字母表里面新的字母，将其替换，
               并且只更换一次。否则相同字母会被连续替换，并且将 repalce 函数的值给予明文本身，
               形成迭代。text = text.f(x) """


print("Finally Ceaser saw this 最终凯撒看到的是:")
print("原始明文：", oringnal)
print("加密密文：", text)


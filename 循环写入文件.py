"""在一个空文档里面写入循环生成的内容，且分行"""

content = []  # 我也不想建立一个列表
test_text = open('rows.txt', 'w')
row = 0
for i in range(1000000):
    row += 1
    print(row)
    content.append('\n')  # 生成换行
    content.append(str(row))  # 目前我只能用列表的方式来写入

test_text.writelines(content)  # 写入缓存，但没真的写入磁盘

test_text.close()  # 关闭文件，真正写入
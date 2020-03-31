import docx  # 引入 docx 文件读写模块


def words_counting(path):
    """计算一个文本文件的字数

    Arguments:
        path {str} -- [带引号的路径，可以使中文]

    Returns:
        [int] -- [这个文本文件总的字数]
    """

    document = docx.Document(path) # 读取文件，可以有是中文路径

    print(type(document))


    para = document.paragraphs  # 段落是一个对象，可以加载对象到变量，实际上是一个列表，或者迭代器？
    print(type(para))
    final_count = 0
    for each_para in para: #遍历这个列表 para
        count = len(each_para.text) # 使用 text 方法拿到文字的长度，text 这个地方感觉也是一个列表。
        print(count)
        final_count = final_count+count  # 计算所有的字数


    return final_count
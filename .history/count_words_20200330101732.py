import docx  # 引入 docx 文件读写模块

def all_path(dirname):
    """[列举一个文件夹下所有文件的绝对路径列表]

    Arguments:
        dirname {[字符串]} -- [文件夹的路径]

    Returns:
        [list] -- [个文件夹下所有文件的绝对路径列表]
    """
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result


def oneFile_words_counting(path):
    """计算一个文本文件的字数

    Arguments:
        path {str} -- [带引号的路径，可以使中文]

    Returns:
        [int] -- [这个文本文件总的字数]
    """
    document = docx.Document(path) # 读取文件，可以有是中文路径
    #print(type(document))
    para = document.paragraphs  # 段落是一个对象，可以加载对象到变量，实际上是一个列表，或者迭代器？
    print(type(para))
    final_count = 0
    for each_para in para: #遍历这个列表 para
        count = len(each_para.text) # 使用 text 方法拿到文字的长度，text 这个地方感觉也是一个列表。
        #print(count)
        final_count = final_count+count  # 计算所有的字数
    return final_count



path_given = '/Users/nordenbox/Dropbox/Words/我的剧本'

list_under_path = all_path(path_given)

for i in list_under_path:
    words_counting_general = oneFile_words_counting(i)
    final_res = final_res+words_counting_general

print(final_res)






import docx

document = docx.Document('/Users/nordenbox/Dropbox/Words/englishpath/百万包子.docx')

print(type(document))


para = document.paragraphs
print(type(para))
final_count = 0
for each_para in para:
    count = len(each_para.text)
    print(count)
    final_count = final_count+count


print(final_count)
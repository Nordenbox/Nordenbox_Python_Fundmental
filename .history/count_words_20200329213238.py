import docx

document = docx.Document('/Users/nordenbox/Dropbox/Words/englishpath/millionbaozi.docx')

print(type(document))


para = document.paragraphs
print(type(para))
for each_para in para:
    count = len(each_para.text)
    print(count)
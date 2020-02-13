import docx

document = docx.opendocx(r'/Users/nordenbox/desktop/History of Warcraft.docx')
num = 0
for i in docx.getdocumenttext(document):
    num += len(i)

print('Total of ',num)
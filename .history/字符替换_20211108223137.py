
test = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
substite01 = 'abcdefghijklmnopqrstuvwxyz' # 替换源
substite02 = 'cdefghijklmnopqrstuvwxyzab' # 替换目标
output = test.maketrans(substite01, substite02) # maketrans 替换后给出的是一个字典，需要转换之后才能看到结果

print(test.translate(output)) # translate 就是转换的作用

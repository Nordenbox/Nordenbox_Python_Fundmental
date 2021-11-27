list = ['AAB', 'BBC', "EEA", 'DDD', 'CCE', 'DDB', "CCB"]
print([i for i in list if 'A' in i or "B" in i])
# 这里不能写成 if A or B in i，这样是不对的。
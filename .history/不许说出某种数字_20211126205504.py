number = int(input('which number can not say(1-10): '))
list = [i for i in range(1,100) if i%number==0 or str(number) in str(i) ]
print(list)
print(f"一共有{len(list)}次")
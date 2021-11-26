number = int(input('which number can not say(1-10): '))
list = [i for i in range(1,100) if i%number==0 or str(number) in str(i) ]
#print(seven)
print(f"一共说了{len(list)}次过")
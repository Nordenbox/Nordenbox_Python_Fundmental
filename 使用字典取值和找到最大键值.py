mountain = {"乔戈里峰":8611,"干城章嘉峰":8586,"珠穆朗玛峰":8844.43,"洛子峰":8516}
c= mountain.values()
print(type(c))
print(c)
a = max(mountain.values()) # values 实际就是一个取键值的办法，
                           # 似乎可以假定mountain.values最后得出来的是一个列表。
#print(a)
for key, values in mountain.items(): # 用两个指针遍历健与键值对
    if (values == a):
        print(f"世界最高峰为{key}，高度为{values}米。")
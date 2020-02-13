def demo(obj) :
    obj += obj
    print("形参值为：",obj)
    
print("-------值传递-----")
a = "#"
print("a的值为：",a)
demo(a)
print("实参值为：",a)
print("-----引用传递-----")
a = [1,2,3]
print("a的值为：",a)
demo(a)
print("实参值为：",a)
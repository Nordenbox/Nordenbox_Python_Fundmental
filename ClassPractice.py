class Student:
    # 初始化函数，为每个实例创建4个参数（其中后3个参数有默认值）
    def __init__(self, name, job=None, time=0.00, time_effective=0.00): 
        self.name = name
        self.job = job
        self.time = time
        self.time_effective = time_effective

    def count_time(self, hour, rate):
        self.time += hour
        self.time_effective += hour * rate  # 有效时间=投入时间×学习效率

student1 = Student('韩梅梅','Student')
print(student1.job)
student1.count_time(10, 0.8)  # 学习效率为0.8
print(student1.time_effective)

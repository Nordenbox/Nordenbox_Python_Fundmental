# 第一行：必不可少的调用模块。
import time
import datetime

input("欢迎使用“时间管理器”！请按回车继续。")

while True:
    task_name = input('请输入任务名：')
    task_time = int(input('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟\n'))
    time.sleep(0.5)
    input('此次任务信息：\n我要完成的任务：%s\n我至少要专注：%d分钟\n按回车开始专注：'%(task_name,task_time))
    # 下面应该要有两行代码，自动记录可以计算以及可以打印的开始时间。
    time_start=time.time()
    time_stamp = datetime.datetime.now()
    print ("当前任务的开始时间" + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))
    

    jishi = task_time*60
    

    print('倒计时开始……')
    for i in range(jishi, 0, -1):
        msg = u"\r任务将在 " + str(i) + "秒 内结束"
        print(msg, end="")
        time.sleep(1)
    end_msg = "结束" + "  "*(len(msg)-len("结束"))  
    print(u"\r"+end_msg)
    

    task_status = input('请在任务完成后按输入y:')
    
    if task_status == 'y':
        time_end=time.time()
        endtime_stamp = datetime.datetime.now()
        print ("当前任务的结束时间" + endtime_stamp.strftime('%Y.%m.%d-%H:%M:%S'))
        


        with open('timelog2.txt','a', encoding = 'utf-8') as f:
            actual_time = time_end - time_start
            f.write(task_name + ' 的预计时长为：' + str(task_time) + '分钟\n')
            f.write(task_name + ' 的实际时长为：' + str(actual_time) + '分钟\n')
            print('任务的预计时长为：' + str(task_time) + '分钟\n'+'当前任务的实际时长是：'+ str(actual_time/60) + '分钟\n')
        again = input('建立一个新任务请按 y, 退出时间日志记录器请按 q：')
        if again == 'q':            
            break
    else:
        print('抱歉，你的输入有误。请重启时间记录器。')

print('愿被你善待的时光，予你美好的回赠。')

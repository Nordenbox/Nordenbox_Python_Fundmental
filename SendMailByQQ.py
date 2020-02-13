import smtplib
from email.mime.text import MIMEText
from email.header import Header


''' 这是一个用于测试的简单发送邮件的程序。'''

# 定义发件人的信箱信息
smtp_server = 'smtp.qq.com'
username = '4664010@qq.com'
password = 'oocwimshjziubhic'
sender = username

# 要求用户输入收件人邮件地址信息
to_addrs = []
while True:
    a = input('请输入收件人邮箱：')
    #输入收件人邮箱
    to_addrs.append(a)
    #写入列表
    b=input('是否继续输入，n退出，回车继续：')
    #询问是否继续输入
    if b == 'n':
        break
print(to_addrs)


# 确定邮件内容
mail_subject = input('请输入你邮件的主题：\n')
mail_text = input('请输入你的邮件内容，不要超过一行。\n')

msg = MIMEText(mail_text,'plain','utf-8')

#发送邮件

msg['From'] = Header(sender)
msg['To'] = Header(','.join(to_addrs))
msg['Subject'] = Header(mail_subject)

server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
server.login(username, password) 
server.sendmail(sender, to_addrs, msg.as_string()) 

#发送完关闭
server.quit()
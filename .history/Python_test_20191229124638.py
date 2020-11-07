import smtplib
from email.mime.text import MIMEText

''' 这是一个用于测试的简单发送邮件的程序。'''


smtp_server = 'smtp-mail.outlook.com'
username ='nordenbox@hotmail.com'
password = 'nord4587.live.com'
sender = 'nordenbox@hotmail.com'
to_addr = '4664010@qq.com'
msg = MIMEText('This is my first Email text, send by python'
               'testing diffrent server','plain','utf-8')

server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 587)
server.login(username, password)
server.sendmail(sender, to_addr, msg.as_string())

server.quit()
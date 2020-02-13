import smtplib
# smtplib 用于邮件的发信动作
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
import csv
# 引用csv模块，用于读取邮箱信息

# 发信方的信息：发信邮箱，QQ邮箱授权码
# 方便起见，你也可以直接赋值
from_addr = '4664010@qq.com'
password = 'oocwimshjziubhic'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮件内容
text='''采用读取 CSV 文件内容读取群发邮件地址列表的邮件。'''

# 待写入csv文件的收件人数据：人名+邮箱
# 记得替换成你要发送的名字和邮箱
data = [['罗登, ' 'nordenbox@hotmail.com'],['罗登', 'nordenbox@gmail.com']]

# 写入收件人数据
with open('to_addrs.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

# 读取收件人数据，并启动写信和发信流程
with open('to_addrs.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader: 
        to_addrs=row[0]
        msg = MIMEText(text,'plain','utf-8')
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addrs)
        msg['Subject'] = Header('python test')
        server = smtplib.SMTP_SSL(smtp_server)
        server.connect(smtp_server,465)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addrs, msg.as_string())

# 关闭服务器
server.quit()
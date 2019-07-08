import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'pythonabc@qq.com'
msg['To'] = 'pythonabc@mail.com'
msg['Subject'] = 'QQMail testing'

msg.attach(MIMEText('Your message from QQ'))

server = smtplib.SMTP_SSL('smtp.qq.com', 465)
server.login('pythonabc@qq.com', 'xuapwdrgxocnddec')
server.send_message(msg)
server.quit()


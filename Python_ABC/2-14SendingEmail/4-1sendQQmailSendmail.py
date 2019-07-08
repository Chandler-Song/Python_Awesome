import smtplib

fromAddr = 'pythonabc@qq.com'
toAddr = 'pythonabc@mail.com'
msg = 'Your message from QQ'

username = 'pythonabc@qq.com'
pswd = 'jdfemszbepdfdhee'

server = smtplib.SMTP_SSL('smtp.qq.com', 465)
header = 'To:' + toAddr + '\n' + 'From: ' + fromAddr + '\n' + 'Subject: QQMail testing \n'
msg = header + msg

server.login(username, pswd)
server.sendmail(fromAddr, toAddr, msg)
server.quit()


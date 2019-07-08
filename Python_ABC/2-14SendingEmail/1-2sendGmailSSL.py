import smtplib
#
fromAddr = 'pythonlink@gmail.com'
toAddr = 'pythonabc@mail.com'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(fromAddr, "jkhgqkypgnrbmmyl")
#
header = 'To:' + toAddr + '\n' + 'From: ' + fromAddr + '\n' + 'Subject: Gmail testing \n'
msg = 'Your Message from Gmail!'
msg = header + msg

#
server.sendmail(fromAddr, toAddr, msg)
server.quit()


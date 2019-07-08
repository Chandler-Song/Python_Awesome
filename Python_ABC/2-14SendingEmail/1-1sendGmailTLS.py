import smtplib
#
fromAddr = 'pythonlink@gmail.com'
toAddr = 'pythonabc@mail.com'


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromAddr, "jkhgqkypgnrbmmyl")
#
header = 'To:' + toAddr + '\n' + 'From: ' + fromAddr + '\n' + 'Subject: testing \n'
msg = 'Your Message from Gmail!'
msg = header + msg

#
server.sendmail(fromAddr, toAddr, msg)
server.quit()
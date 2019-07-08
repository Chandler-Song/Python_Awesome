import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#
fromAddr = "pythonlink@gmail.com"
myPass = "jkhgqkypgnrbmmyl"
toAddr = "pythonabc@mail.com"
#
msg = MIMEMultipart()
msg['From'] = fromAddr
msg['To'] = toAddr
msg['Subject'] = "Narcissistic Cannibal!"
#
body = '''
Don't wanna be sly and defile you
Desecrate my mind and rely on you
I just wanna break this crown
But it's hard when I'm so run down
And you're so cynical
Narcissistic cannibal
Got to bring myself back from the dead
'''
msg.attach(MIMEText(body, 'plain'))
# msg.attach(MIMEText(body))
#
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(fromAddr, myPass)
text = msg.as_string()
server.sendmail(fromAddr, toAddr, text)
# server.send_message(msg)
server.quit()
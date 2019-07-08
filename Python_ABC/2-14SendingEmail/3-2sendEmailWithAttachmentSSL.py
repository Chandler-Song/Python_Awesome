#https://docs.python.org/3.5/library/email-examples.html

import smtplib
#
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
#
fromAddr = "pythonlink@gmail.com"
myPass = "jkhgqkypgnrbmmyl"
toAddr = "pythonabc@mail.com"

# create container email message
msg = MIMEMultipart()
msg['Subject'] = "Sunset"
msg['From'] = fromAddr
msg['To'] = toAddr
# msg.preamble = "When the sun has set, no candle can replace it."
body = "When the sun has set, no candle can replace it.\n\n\n"
#
msg.attach(MIMEText(body, 'plain'))
#
with open('sunset.jpg', 'rb') as fp:
	img = MIMEImage(fp.read())
#
msg.attach(img)
#
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(fromAddr, myPass)
#
server.send_message(msg)

#
server.quit()
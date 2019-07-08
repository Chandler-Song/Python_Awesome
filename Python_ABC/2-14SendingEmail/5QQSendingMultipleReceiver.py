# # http://blog.csdn.net/zl87758539/article/details/53363860
#
from email.mime.text import MIMEText
import smtplib
#
mailto_list = ["pythonabc@mail.com","pythonlink@gmail.com"]
#
mail_host = "smtp.qq.com"
mail_user = "pythonabc"
mail_pass = "xuapwdrgxocnddec"
#
#==========================================
# 发送邮件
#==========================================
def send_mail(to_list, sub, content):
  '''''
  to_list:发给谁
  sub:主题
  content:内容
  send_mail("xxx@xxxx.com","主题","内容")
  '''
#
  msg = MIMEText(content)
  msg['Subject'] = sub
  msg['From'] = 'PythonABC@qq.com'
  msg['To'] = ";".join(to_list)
#
  try:
    s = smtplib.SMTP_SSL(mail_host, 465)
    # s.set_debuglevel(1)
    s.login(mail_user,mail_pass)
    s.send_message(msg)
    s.close()
    return True
#
  except Exception as e:
    print(e)
    return False
#
if send_mail(mailto_list,"群发邮件","试试可不可以"):
    print("发送成功")
else:
    print("发送失败")
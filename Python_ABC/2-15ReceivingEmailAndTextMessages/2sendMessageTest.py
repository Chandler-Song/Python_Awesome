from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console

account_sid = "ACbe036e2467f6b1b9b7eea6be626ef0a7"
auth_token = "965ef4f100fe04b96a4b8886a7fd338d"
client = Client(account_sid, auth_token)


myTwilioNumber = '+15109013265'
myCellPhone = '+8613912345678'
# +86 13912345678
client.messages.create(to=myCellPhone, body='昨夜西风凋碧树，望断天涯路',
								 from_=myTwilioNumber,
								 )

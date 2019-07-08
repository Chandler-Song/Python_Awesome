# textMyself.py - Defines the textmyself() function that texts a message
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console

# Preset values:
accountSID = "ACbe036e2467f6b1b9b7eea6be626ef0a7"
authToken = "209a46d78c1559e0dda0fd483e3a496f"
myTwilioNumber = '+19727553368'
myCellPhone = '+8613912345678'

def textMyself(message):
	client = Client(accountSID, authToken)
	client.messages.create(to=myCellPhone, body= message,
								 from_=myTwilioNumber
								 )
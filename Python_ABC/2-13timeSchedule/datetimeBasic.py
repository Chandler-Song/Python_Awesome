import datetime
import time

# A unix epoch timstamp can be converted to a datetime object
# print(time.time())
# print(datetime.datetime.fromtimestamp(time.time()))
# print(datetime.datetime.fromtimestamp(10000000))
#
#
# dn = datetime.datetime.now()
# # return a datetime oject
# print(dn)
# print('year:{}, month:{}, day:{},'
# 	  ' hour:{}, minute:{}, second:{}'.format(dn.year,
# 						dn.month, dn.day, dn.hour, dn.minute, dn.second))
#
# dt = datetime.datetime(2017, 12, 20, 19, 16, 0)
# print('year:{}, month:{}, day:{},'
# 	  ' hour:{}, minute:{}, second:{}'.format(dt.year,
# 						dt.month, dt.day, dt.hour, dt.minute, dt.second))

# datetime objects can be compared, the later datetime object is the 'greated' value.
# springFestival = datetime.datetime(2018, 2, 16, 0, 0, 0)
# chrismas = datetime.datetime(2017, 12, 25, 0, 0, 0)
# dec252017 = datetime.datetime(2017, 12, 25, 0, 0, 0)
# #
# print(chrismas != dec252017)
# print(springFestival > chrismas)

# titedelta represents a duration of time rather than a moment in time
# delta = datetime.timedelta(weeks=1, days=11, hours=10, minutes=9, seconds=8)
# # to create a timedelta object
#
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
#
# # passing a timedelta object to str() will return a nicely formated, human-readable string
# # representation fo the object
# print(str(delta))

# dt = datetime.datetime.now()
# thousandDays = datetime.timedelta(days=1000)
# print(dt + thousandDays)
# print(dt - thousandDays)


newYear2018 = datetime.datetime(2018, 1, 1)
while datetime.datetime.now() < newYear2018:
	time.sleep(1)

# Converting datetime object into string
# oct21st = datetime.datetime(2017, 10, 21, 16, 29, 0)
# print(oct21st.strftime('%Y/%m/%d %H:%M:%S'))
# print(oct21st.strftime('%I:%M %p'))
# print(oct21st.strftime("%B of '%y"))
#
#
# print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
# print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
# print(datetime.datetime.strptime("October of '15", "%B of '%y"))
# print(datetime.datetime.strptime("November of '63", "%B of '%y"))




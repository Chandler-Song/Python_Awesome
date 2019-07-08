#
# def change_name():
# 	return 'Mark'
#
# name = 'Tom'
# name = change_name()
# print(name)
#


def get_sum(*args):
	sum = 0
	for i in args:
		sum += i
	return sum

print("Sum =", get_sum(3, 4))






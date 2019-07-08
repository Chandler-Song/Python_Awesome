# def spam(divideBy):
#     return 42/divideBy
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))


def spam(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		# pass
		# print('出错：0 不被接受')
		print('Error: Invalid argument')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


#
# try:
# 	pass
# except Exception:
# 	pass
# else:
# 	pass
# finally:
# 	pass

# f = open('testfile.txt')
# print(f.read())

# try:
# 	f = open('testfile.txt')
# 	print(f.read())
# except Exception:
# 	print('Sorry, this file does not exist')

# f = open('testfile.txt')
# print(f.read())

# try:
# 	f = open('testfile.txt')
# except FileNotFoundError:
# 	print('Sorry, this file does not exist')
# except:
# 	print('sorry, something is wrong')

#
# try:
# 	f = open('heine.txt')
# except FileNotFoundError:
# 	print('Sorry, this file does not exist')
# except:
# 	print('sorry, something is wrong')
# else:
# 	print(f.read())
# 	f.close()


# var = bad_var
# print(var)
#
bad_var = 'I am not bad_var'
try:
	var = bad_var
except NameError as e:
	print(e)
else:
	print(var)
finally:
	print("Executing Finally...")








import time

# print(time.time())

# time.time(): to measure how long a piece of code takes to run

# Calculate the product of the first 100000 numbers
def calcProd():
	product = 1
	for i in range(1, 100000):
		product = product * i
	return product
#
startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is {} digits long'.format(len(str(prod))))
print('Take {} seconds to calculate'.format(endTime - startTime))

# time.sleep()
# for i in range(3):
# 	print('Tick')
# 	time.sleep(1)
# 	print('Tick')
# 	time.sleep(1)


# round()
# now = time.time()
# print(now)
# print(round(now,2))
# print(round(now,4))
# print(round(now))



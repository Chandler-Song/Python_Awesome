# ---------- LIST COMPREHENSIONS ----------
# import random
#
# li = [9,1,8,2,7,3,6,4,5]
# print(li)
#
# numList = []
# for i in range(5):
# 	numList.append(random.randrange(1, 10))
#
# print(numList)

# nList = [i*2 for i in range(10)]
# print(nList)
'''
1 2 3 4
2 3 4 5
4 5 6 7

'''
# numList = [1,2,3,4,5]
# print(numList)
#
# pList = [pow(i, 3) for i in numList]
# print(pList)
#
# listOfValue = [[pow(i, 2), pow(i, 3), pow(i, 4)] for i in numList]
# print(listOfValue)
#
# print()
# for k in listOfValue:
# 	print(k)
# print()

print("hope" * 3)
print([0] * 10)

multiDList = [[0]*10 for i in range(10)]
for k in multiDList:
	print(k)
print()

multiDList[0][1] = 10
for k in multiDList:
	print(k)



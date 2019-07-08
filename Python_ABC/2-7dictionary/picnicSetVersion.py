# Guest & items
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1,'chicken wing':10}}

# function: get amount of a item(allGuests, item)
def totalBrought(guests, item):

	# initiate a counter
	numBrought = 0

	# traverse values of all guests
	for v in guests.values():
			# accumulate the item
			numBrought += v.get(item, 0)

	return numBrought

foodSet = set()
for v in allGuests.values():
	foodSet |= set(v)
# print number of items (call function)
print("Number of things being brought: \n")

for food in foodSet:
	print("-{:20}				{}".format(food, totalBrought(allGuests, food)))

# print("-Apple				{}".format(totalBrought(allGuests, 'apples')))
# print("-Cups  				{}".format(totalBrought(allGuests, 'cups')))
# print("-Pretzel  			{}".format(totalBrought(allGuests, 'pretzels')))
# print("-Ham Sandwiches  	{}".format(totalBrought(allGuests, 'ham sandwiches')))
# print("-Apple  Pies 		{}".format(totalBrought(allGuests, 'apple pies')))






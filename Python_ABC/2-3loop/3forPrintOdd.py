# ---- PROBLEM : PRINT ODDS FROM 1 to 20 ----------

# Use for loop through the list from 1 to 21
for i in range(1, 21):

	# Use modulus to check that the result is equal to 0 or not
	if (i % 2) != 0:

		# print the odds
		print('i = ', i)

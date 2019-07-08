# 1 + 2 + 3 + 4 + ... + 99 + 100

# Empty sum variable
total = 0

# Use loop to accumulate 1 to 100
for num in range(101):
	total += num

# Print out the result
print('1 + 2 + 3 + ... + 100 = ', total)

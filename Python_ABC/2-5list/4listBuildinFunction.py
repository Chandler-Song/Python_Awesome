# ---------- MORE LIST FUNCTIONS ----------
import random

numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))

print(numList)

# Sort a list
numList.sort()
print(numList)

# Reverse a list
numList.reverse()
print(numList)

# Insert value at index insert(index, value)
numList.insert(5, 10)
print(numList)

# Delete first occurrence of value
numList.remove(10)
print(numList)

# Remove item at index
numList.pop(2)
print(numList)
# ---------- STRING METHODS ----------

# Strings have many methods we can use beyond what I covered last time
rand_string = "   life is a beautiful struggle   "
print(rand_string)

# Delete whitespace on left
rand_string = rand_string.lstrip()
print(rand_string)


# Delete whitespace on right
rand_string = rand_string.rstrip()

# Delete whitespace on right and left
rand_string = rand_string.strip()

print(rand_string)
print()

# Capitalize the 1st letter
print(rand_string.capitalize())

# Capitalize every letter
print(rand_string.upper())

# lowercase all letters
print(rand_string.lower())

# Turn a list into a string and separate items with the defined
# separator
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))
print(",".join(a_list))

# Convert a string into a list
a_list_2 = rand_string.split()

for i in a_list_2:
    print(i)

# Count how many times a string occurs in a string
print("How many is :", rand_string.count("if"))

# Get index of matching string
print("Where is 'is' :", rand_string.find("is"))

# Replace a substring
print(rand_string.replace("struggle", "journey"))
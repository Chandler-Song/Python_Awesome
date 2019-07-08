# Complete birthday database

# current database
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
print(birthdays)

# loop to perfect birthday database
while True:

	# input name which decides next step
	name = input("Enter a name(blank to quit): ")

	# exit, exist already, no record
	if name == '':
		break
	elif name in birthdays:
		print('{} is the birthday of {}'.format(birthdays[name], name))
	else:
		print('I do not have birthday information for ', name)
		bday = input('What is the birthday? ')
		birthdays[name] = bday
		print('Birthday database updated')

print(birthdays)
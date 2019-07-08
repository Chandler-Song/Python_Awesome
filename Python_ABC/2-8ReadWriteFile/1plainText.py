# Jeanette = open('Jeanette.txt')
# quote = Jeanette.read()
# print(quote)
# print(Jeanette.closed)
# Jeanette.close()
# print(Jeanette.closed)
#
#
# with open('Jeanette.txt', mode='a+') as Jeanette:
# 	Jeanette.write("\nFrom Jeanette\n")
# 	Jeanette.seek(0)
# 	quote = Jeanette.read()
# 	print(quote)
# 	print(Jeanette.name)
# print(Jeanette.closed)

# with open('Jeanette.txt', mode='w') as Jeanette:
# 	Jeanette.write("\nLook what I did!\n")
# with open('Jeanette.txt') as Jeanette:
# 	print(Jeanette.read())
#
# with open('Jeanette.txt', mode='w+') as Jeanette:
# 	Jeanette.write("\nLook what I did!\n")
# 	Jeanette.seek(0)
# 	print(Jeanette.read())
# #
# with open('Jeanette.txt', mode='r+') as Jeanette:
# 	print(Jeanette.tell())
# 	print(Jeanette.read())
# 	print(Jeanette.tell())
# 	Jeanette.seek(10)
# 	Jeanette.write("mess!")
# 	print(Jeanette.tell())
# 	print(Jeanette.read())
# 	Jeanette.seek(0)
# 	print(Jeanette.read())
#
with open('Jeanette.txt',mode='w') as Jeanette:
	Jeanette.write('''I’ll call you, and we’ll light a fire, and drink some wine, and recognise each other in the place that is ours.
Don’t wait. Don’t tell the story later. Life is so short. This stretch of sea and sand, this walk on the beach before the tide covers everything we have done.
I love you.
The three most difficult words in the world.
But what else can I say?
''')
# #
# with open('Jeanette.txt') as Jeanette:
# 	for line in Jeanette:
# 		print(line, end='')
# 	print()

# with open('heine.txt') as heine:
# 	f_content = heine.read()
# 	print(f_content)
#
with open('Jeanette.txt') as Jeanette:
	f_content = Jeanette.readlines()
	print(f_content)
print()
#
# with open('Jeanette.txt') as Jeanette:
# 	f_content = Jeanette.readline()
# 	print(f_content,end='')
# 	f_content = Jeanette.readline()
# 	print(f_content,end='')
# 	f_content = Jeanette.readline()
# 	print(f_content,end='')

# with open('Jeanette.txt') as Jeanette:
# 	f_content = Jeanette.read(100)
# 	print(f_content)
# 	f_content = Jeanette.read(100)
# 	print(f_content)
# 	f_content = Jeanette.read(100)
# 	print(f_content)
# #
#
# # big file
# with open('heine.txt') as heine:
#
# 	size_to_read = 100
# 	f_content = heine.read(size_to_read)
#
# 	while len(f_content)>0:
# 		print(f_content, end='')
# 		f_content = heine.read(size_to_read)
#
with open('Jeanette.txt') as Jeanette:
	size_to_read = 10
	f_content = Jeanette.read(size_to_read)

	while len(f_content)>0:
		print(f_content, end='*')
		f_content = Jeanette.read(size_to_read)










items = {"arrow","spear","arrow","arrow","rock"}
print(items)

print(len(items))

if "clock" in items:
	print("Rock exist")
else:
	print("Not found")

pets = set()

pets.add('cat')
pets.add('dog')
pets.add('gerbil')
print(pets)
pets.discard('cat')
print(pets)
pets.discard(('zebra'))

numbers1 = {1,2,3,4,7}
numbers2 = {1,3,4,6}
print(numbers1 | numbers2)
print(numbers1 & numbers2)
print(numbers1 - numbers2)

numbers2.update([10, 20,40,50])
print(numbers2)

dict1 = {"cat":1,"dog":2,"bird":3}
print(dict1)
keys = set(dict1)
print(keys)

for i in set('apple'):
	print(i,end=',')
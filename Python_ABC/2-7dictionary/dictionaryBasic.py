myCatList = ['Garfield','orange','fat']
yourCatList = ['orange','fat','Garfield']
print(myCatList == yourCatList)

myCat = {'name':'Garfield','color':'orange','size':'fat'}
yourCat = {'color':'orange','size':'fat','name':'Garfield'}
print(myCat == yourCat)

# print('My cat\'s name is:',myCat['name'])
# print('My cat\'s name is:',myCatList[0])
# print()
myCat['city'] = 'Xiamen'
# print(myCat)
myCat['color'] = 'orange tabby'
# print(myCat)
print()

print(myCat.values())

for v in myCat.values():
	print(v, end=', ')
print('\n')

print(myCat.keys())

for v in myCat.keys():
	print(v, end=', ')
print('\n')

print('\n')

print(myCat.items())

for k,v in myCat.items():
	print(v, end=', ')
print('\n')

print('Is there a city: ', "Garfield" in myCat)
print('Is there a city: ', "Garfield" in myCat.values())
print('Is there a city: ', "city" in myCat.keys())
print('Is there a city: ', "hobby" in myCat)
print('\n')

print(myCat.get("name","Not Here"))
print(myCat.get("hobby","Not Here"))
print('\n')

print(myCat)
# del myCat['city']
print(myCat)

myCat.clear()
print(myCat)
print('\n')

picnicItems = {'apple':5, 'cup':10}
picnicItems['bacon'] = 7
print(picnicItems)
picnicItems.setdefault('sausage',0)
print(picnicItems)
picnicItems.setdefault('apple',3)
print(picnicItems)
print('\n')

print('We have {} apples and {} eggs'.format(picnicItems.get('apple',0),picnicItems.get('egg',0)))



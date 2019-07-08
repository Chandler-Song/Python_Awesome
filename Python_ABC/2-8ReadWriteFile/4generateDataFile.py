import pprint

cats = [{'name':'Garfield','desc':'chubby'},
		{'name':'Tom','desc':'naught'},
		{'name':'kitty','desc':'pretty'}]

s = pprint.pformat(cats)
print(s)
with open('myCats.py','w') as fileObj:

	fileObj.write('cats = '+ s + '\n')



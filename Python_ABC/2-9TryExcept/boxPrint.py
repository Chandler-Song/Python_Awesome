'''
****
*  *
*  *
****

oooooooooooooooooooo
o                  o
o                  o
o                  o
oooooooooooooooooooo
'''

def boxPrint(symbol, width, heigth):

	if len(symbol) != 1:
		raise Exception('Symbol must be a single character. ')
	if width <= 2:
		raise Exception('Width must be greater than 2. ')
	if heigth <= 2:
		raise Exception('Height must be greater than 2. ')
	print(symbol * width)

	for i in range(heigth - 2):
		print(symbol + ' ' * (width - 2) + symbol)

	print(symbol * width)
	print()

for sys, w, h in (('*', 4, 4), ('0', 20, 2), ('x', 2, 3), ('ZZ', 3, 3)):
	try:
		boxPrint(sys, w, h)
	except Exception as err:
		print('An exception happened: ' + str(err) +'\n')
# readCensusExcel.py - Tabulates population and number of census tracts
# for each county.

import openpyxl, pprint

# Read the spreadsheet data
print('Opening workbook')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active

countryData = {}

# Fill in countryData with each city's pop and tracts
for row in range(2, sheet.max_row+1):

	# Each row in the spreasheet has data
	state = sheet['B' + str(row)].value
	country = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value

	# make sure the key state exists
	countryData.setdefault(state, {})
	# make sure the key for country in state exists
	countryData[state].setdefault(country,{'tracts':0, 'pop':0})
	# Each row represents one census tract, so increment by one
	countryData[state][country]['tracts'] += 1
	# Increase the country pop by the pop in this census tract
	countryData[state][country]['pop'] += int(pop)

# Open a new text file and write the contents fo countryData to it
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countryData))


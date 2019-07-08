# readCensusExcel.py - Tabulates population and number of census tracts
# for each county.

import openpyxl
import docx

# Read the spreadsheet data
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

countryData = {}
stateData = {}

# Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exists.
    countryData.setdefault(state, {})
    # Make sure the key for this county in this state exists.
    countryData[state].setdefault(county, {'tracts': 0, 'pop': 0})

    # Each row represents one census tract, so increment by one.
    countryData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract.
    countryData[state][county]['pop'] += int(pop)


    stateData.setdefault(state, 0)
    stateData[state] += int(pop)


# Open a new text file and write the contents of countyData to it.
print('Writing results...')
doc = docx.Document()

table = doc.add_table(rows=1, cols=2)
table.style = 'Light Grid Accent 1'

# Table head
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'State'
hdr_cells[1].text = 'Population'

for stateName, statistic in stateData.items():
        row_cells = table.add_row().cells
        row_cells[0].text = stateName
        row_cells[1].text = str(statistic)

doc.save('PopulationStatistic.docx')
print('Done.')


# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

import csv
import shutil
import pathlib

# assign the path of source and destination folder
srcPath = '/Users/Smonkey/Documents/Python/PythonABC_Online/2-17CSV/removeCsvHeader/'
destPATH = '/Users/Smonkey/Documents/Python/PythonABC_Online/2-17CSV/headerRemoved/'
#
withHeaderPath = pathlib.Path(srcPath)
withoutHeaderPath = pathlib.Path(destPATH)

# copy original folder or files
if not withoutHeaderPath.exists():
    shutil.copytree(srcPath, destPATH)
else:
    for f in [x for x in withHeaderPath.iterdir() if x.is_file]:
        shutil.copy(str(f), destPATH)

# Loop through every file in the current working directory.
for csvFilename in withoutHeaderPath.iterdir():
#
    if not csvFilename.name.endswith('.csv'):
        continue # skip non-csv files
#
    # print('Removing header from ' + str(csvFilename )+ '...')
    print('Removing header from ' + csvFilename.name + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue # skip first row
        csvRows.append(row)
    csvFileObj.close()
#
    # Write out the CSV file.
    csvFileObj = open(csvFilename, 'w')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
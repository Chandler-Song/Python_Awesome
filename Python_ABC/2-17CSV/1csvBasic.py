import csv
import pprint

# Reader object
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)

# #
# exampleData = list(exampleReader)
# pprint.pprint(exampleData)
# #
# print(exampleData[0][2])
# print(exampleData[1][1])
# print(exampleData[6][0])


# csv.reader: How do I return to the top of the file?
# exampleFile.seek(0)
# for row in exampleReader:
	# print('Row #'+ str(exampleReader.line_num) + str(row))
	# print('Row #', exampleReader.line_num, row)
# exampleFile.close()

# The Reader object can be looped over only once. To reread the CSV file,
# you must call csv.reader to create a Reader object.

# writer object
# outputFile = open('output.csv', 'w')
# windows: outputFile = open('output.csv', 'w', newline='')
# If you forget the newline='' keyword argument in open(),
# the CSV file will be double-spaced.

# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow([1, 2, 3.141592, 4])
# outputFile.close()

# The delimiter and lineterminator Keyword Arguments
# csvFile = open('example.tsv', 'w')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# csvWriter.writerow(['apples', 'oranges', 'grapes'])
# csvWriter.writerow(['eggs', 'bacon', 'ham'])
# csvWriter.writerow(['salad', 'salad', 'salad', 'salad', 'salad', 'salad', 'salad', 'salad'])
# csvFile.close()
import PyPDF2

with open('pdfFileReaderDoc.pdf', 'rb') as pdfFileObj:
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	numpages = pdfReader.numPages
	print("Now I know there are {} pages\n".format(numpages))

	if pdfReader.isEncrypted:
		if pdfReader.decrypt('python'):
			pageObj = pdfReader.getPage(0)
		else:
			print('Wrong password')
	else:
		pageObj = pdfReader.getPage(0)

	print(pageObj.extractText())

	pageObj.rotateClockwise(90)
	pdfwriter = PyPDF2.PdfFileWriter()
	pdfwriter.addPage(pageObj)
	pdfwriter.addBlankPage()
	with open('rotatedPDF.pdf', 'wb') as rotatedPDF:
		pdfwriter.write(rotatedPDF)
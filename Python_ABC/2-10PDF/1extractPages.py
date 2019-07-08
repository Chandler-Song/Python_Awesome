import PyPDF2

with open('withCover.pdf', 'rb') as pdfWithCover:

	pdfReader = PyPDF2.PdfFileReader(pdfWithCover)
	pdfWriter = PyPDF2.PdfFileWriter()

	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)

	with open('withoutCover.pdf', 'wb') as pdfOutputFile:
		pdfWriter.write(pdfOutputFile)

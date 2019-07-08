import PyPDF2

with open('PythonABC.pdf', 'rb') as pdfFile:

	pdfReader = PyPDF2.PdfFileReader(pdfFile)

	pdfWriter = PyPDF2.PdfFileWriter()

	for pageNum in range(pdfReader.numPages):
		pdfWriter.addPage(pdfReader.getPage(pageNum))

	pdfWriter.encrypt('python')

	with open('encryptedPythonABC.pdf', 'wb') as resultPdf:
		pdfWriter.write(resultPdf)
import PyPDF2

pdfFile = open('withCover.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
coverPage = pdfReader.getPage(0)

markFile = open('watermark.pdf', 'rb')
pdfWatermarkReader = PyPDF2.PdfFileReader(markFile)

coverPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(coverPage)

for pageNum in range(1, pdfReader.numPages):
	pageObj = pdfReader.getPage(pageNum)
	pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)

pdfFile.close()
markFile.close()
resultPdfFile.close()



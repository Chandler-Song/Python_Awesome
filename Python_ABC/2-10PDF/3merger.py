import PyPDF2

filenames = ['startCover.pdf', 'basic.pdf', 'notDream.pdf',  'instance.pdf','endCover.pdf']

merger = PyPDF2.PdfFileMerger()
for filename in filenames:
	merger.append(PyPDF2.PdfFileReader(filename))
merger.write('PythonABC.pdf')

# filenames = ['startCover.pdf', 'basic.pdf']
#
# merger = PyPDF2.PdfFileMerger()
# for filename in filenames:
# 	merger.append(PyPDF2.PdfFileReader(filename))
# merger.write('withCover.pdf')
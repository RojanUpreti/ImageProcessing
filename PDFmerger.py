import PyPDF2
import sys

inputs=sys.argv[1:]
def pdf_combiner(pdf_list):
	for pdf in pdf_list:
		print(pdf)
pdf_combiner(inputs)
merger=PyPDF2.pdfFileMerger()
merger.append(pdf)
merger.write('super.pdf')

#python PDFmerger.py dummy.pdf twopage.pdf tilt.pdf
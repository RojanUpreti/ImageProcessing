import PyPDF2
template=PyPDF2.pdfFileReader(open('super.pdf','rb'))
watermark=PyPDF2.pdfFileReader(open('wtr.pdf','rb'))
output=PyPDF2.pdfFileWriter()
for i in range(template.getNumPages()):
	page=template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('watermarked_output.pdf','wb') as file:
		output.write(file)

#python Watermarker.py
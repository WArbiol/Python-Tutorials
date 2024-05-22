import PyPDF2

# import glob
# pdfs = sorted(glob.glob('./*.pdf'))

pdfs = ['pdf1.pdf', 
	'pdf2.pdf',
        'pdf3.pdf']

writer = PyPDF2.PdfWriter()
for pdf in pdfs:
    reader = PyPDF2.PdfReader(pdf)
    pages = reader.pages
    for i, page in enumerate(pages):
        # if pdf != "Q1.pdf" or i != 1:
        #     page.scale_to(width=595, height=842)
        # else:
        #     page.scale_to(width=595, height=120)
        writer.add_page(page)


output = open('seu_output.pdf', 'wb')
writer.write(output)
output.close()

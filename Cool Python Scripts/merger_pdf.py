import PyPDF2

# import glob
# pdfs = sorted(glob.glob('./*.pdf'))

pdfs = ['Dreams onto the Path_compressed (1)1.pdf', 'Dreams onto the Path_compressed (1)2.pdf',
        'Dreams onto the Path_compressed (1)3.pdf']

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


output = open('Dreams onto the Path.pdf', 'wb')
writer.write(output)
output.close()

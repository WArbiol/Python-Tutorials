import PyPDF2, os

src_file = 'nome_do_pdf.pdf'
number_of_splits = 4

with open(src_file, 'rb') as act_mls:
    reader = PyPDF2.PdfReader(act_mls)
    pages = reader.pages
    total_pages = len(pages)
    batch_size = total_pages//number_of_splits
    init = 0
    end = batch_size
    for i in range(number_of_splits):
        writer = PyPDF2.PdfWriter()
        for _, page in enumerate(pages[init:end]):
            writer.add_page(page)
        with open(f"{i+1}.pdf", 'wb') as out_pdf: writer.write(out_pdf)
        init+=batch_size
        end+=batch_size
        if end+batch_size>total_pages: end = total_pages


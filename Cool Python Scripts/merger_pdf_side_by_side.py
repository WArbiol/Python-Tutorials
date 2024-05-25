from PyPDF2 import PdfReader, PdfWriter, PageObject, Transformation
from time import sleep
import os
#Open the files that have to be merged
pdf1 = open('Secrets_of_Cold_War_Technology_by.Gerry.Vassilatos_ISBN0945685203.pdf', 'rb')
pdf2 = open('noIMG.pdf', 'rb')

#Read the files that you have opened
reader1 = PdfReader(pdf1)
reader2 = PdfReader(pdf2)
output = PdfWriter()
j = 1

h=reader1.pages[1].mediabox.height

for i, page1, page2 in zip(range(len(reader1.pages)), reader1.pages, reader2.pages):
    

    # if i!=118: continue

    if page1.annotations:
            page1.annotations.clear()
    
    # print((i+1)/4.75)
    # if i in [0, 1]:
    #     output.add_page(reader1.pages[i])
    #     continue
    # if i in [2, 469, 470, 472, 474]: continue
    # if i == 471:
    #     output.add_page(reader1.pages[236])
    #     continue
    # if i == 473:
    #     output.add_page(reader1.pages[237])
    #     continue
    w = page2.mediabox.width
    page3 = PageObject.create_blank_page(width=w*2, height=h)
    page3.merge_page(page2)
    page3.add_transformation(Transformation().translate(w, 0)) # 118

    # if i%2==0 and i>117:
    #     page4 = PageObject.create_blank_page(width=w*2, height=h)
    #     page4.merge_page(page1)
    #     page4.add_transformation(Transformation().translate(-w, 0)) # 118
    #     page4.merge_page(page3)
    #     output.add_page(page4)
    # else:
    #     page3.merge_page(page1)
    #     output.add_page(page3)
    page3.merge_page(page1)
    output.add_page(page3)



with open('out.pdf', 'wb') as f:
    output.write(f)
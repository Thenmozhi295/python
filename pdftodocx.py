from pdf2docx import Converter
pdf_file = 'D:\python\Thenmozhi.pdf'
docx_file = 'D:\python\Thenmozhi.docx'
# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()
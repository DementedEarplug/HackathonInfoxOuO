import sys
import PyPDF2
from PIL import Image
import img_extractor

# contents = page0.extractText()
# print(contents.encode('utf-8'))
# output = PyPDF2.PdfFileWriter()
# output.addPage(page0)
# outputStream = open("test.pdf", "wb")
# output.write(outputStream)

# print(page0['/Resources'])

# path = 'Impositioned.pdf'

path = 'single_documents/publisher_1.pdf'

pdf = open(path, "rb")

reader = PyPDF2.PdfFileReader(pdf)

page0 = reader.getPage(0)
page1 = reader.getPage(1)

if '/XObject' in page0['/Resources']:
    xObject = page0['/Resources']['/XObject'].getObject()
    # print(xObject)
    # print(xObject['/Im1']['/Resources']['/XObject'])
    img_extractor.extractImages(xObject)
    img_extractor.extractImages(xObject['/Im1']['/Resources']['/XObject'])

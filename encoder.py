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

images = []

def encode(resource):
    if '/XObject' in resource['/Resources']:
        xObject = resource['/Resources']['/XObject'].getObject()
        for xo in xObject:
            # print(xObject[xo])
            # print()
            if '/Image' in xObject[xo]['/Subtype']:
                images.append(xObject[xo])
            elif '/Form' in xObject[xo]['/Subtype']:
                encode(xObject[xo])
    return images


xos = {}

def getXObjects(resource):
    if '/XObject' in resource['/Resources']:
        xObject = resource['/Resources']['/XObject'].getObject()
        for xo in xObject:
            print(xObject[xo])
            # print()
            if '/Image' in xObject[xo]['/Subtype']:
                xos[xo] = xObject[xo]
            elif '/Form' in xObject[xo]['/Subtype']:
                encode(xObject[xo])
    return xos



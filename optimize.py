import PyPDF2
import encoder
import img_extractor


path = 'Impositioned.pdf'
path2 = 'deleted.pdf'

images = encoder.encode(PyPDF2.PdfFileReader(open(path, "rb")).getPage(0))

print images

pdf = PyPDF2.PdfFileReader(open(path2, "rb"))


output = PyPDF2.PdfFileWriter()

for page in pdf.pages:
    images = encoder.encode(pdf.getPage(0))
    page = encoder.deleteReferences(page, images)
    images = encoder.encode(page)
    output.addPage(page)

outputStream = open("optimized.pdf", "wb")
output.write(outputStream)

outputStream.close()


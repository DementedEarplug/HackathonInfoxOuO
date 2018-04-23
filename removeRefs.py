import PyPDF2
import encoder
import img_extractor


path = 'Impositioned.pdf'
path2 = 'deleted.pdf'

pdf = PyPDF2.PdfFileReader(open(path, "rb"))

images = encoder.encode(pdf.getPage(0))

print images

output = PyPDF2.PdfFileWriter()

for page in pdf.pages:
    images = encoder.encode(pdf.getPage(0))
    page = encoder.deleteReferences(page, images)
    images = encoder.encode(page)
    output.addPage(page)

outputStream = open("deleted.pdf", "wb")
output.write(outputStream)

outputStream.close()

# # #Mergin OG reference to deleted.pdf
# pdf2 = PyPDF2.PdfFileReader(open(path2, "rb"))

# reader = PyPDF2.PdfFileReader(pdf2)
# output = PyPDF2.PdfFileWriter()

# for page in reader.pages:
#     images = encoder.encode(reader.getPage(0))
#     page = encoder.deleteReferences(page, images)
#     images = encoder.encode(page)
#     output.addPage(page)

# outputStream = open("Optimized.pdf", "wb")
# output.write(outputStream)
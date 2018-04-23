import PyPDF2
import encoder


path = 'Impositioned.pdf'

pdf = open(path, "rb")
#Create a PDF file reader object with Impositioned.pdf
reader = PyPDF2.PdfFileReader(pdf)

#Extract all the images in page 1 to serve as reference
#for the document.
images = encoder.encode(reader.getPage(0))


#Create a PDF file writter object to apply changes.
output = PyPDF2.PdfFileWriter()


#Iterate over the pages in Impositioned.pdf and change the
#references to the ones in the images dictiionary.
for page in reader.pages:
    images = encoder.encode(reader.getPage(0))
    page = encoder.merge(page, images)

    images = encoder.encode(page)

    # print(len(images))

    # for image in images:
    #     print(image)
    #     print()

    #Add changes to new Pdf
    output.addPage(page)

#write changes to new pdf and save as optimized.pdf
outputStream = open("optimized.pdf", "wb")
output.write(outputStream)

path = 'optimized.pdf'

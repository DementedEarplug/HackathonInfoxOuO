import PyPDF2
import encoder
import img_extractor


path = 'Impositioned.pdf'

pdf = open(path, "rb")

reader = PyPDF2.PdfFileReader(pdf)

images = encoder.encode(reader.getPage(0))

# print(len(images))
#
# for image in images:
#     print(image)
#     print()
#
# print("******NEXT PAGE******")


output = PyPDF2.PdfFileWriter()

# for i in range(0, len(reader.pages)):
#     page = reader.getPage(i)
#     page = encoder.merge(page, images)
#     # output.addPage(page)

for page in reader.pages:
    images = encoder.encode(reader.getPage(0))
    page = encoder.merge(page, images)

    images = encoder.encode(page)

    print(len(images))

    for image in images:
        print(image)
        print()

    output.addPage(page)

outputStream = open("optimized.pdf", "wb")
output.write(outputStream)

path = 'optimized.pdf'

# images = encoder.encode(reader.getPage(0))
#
# print(len(images))
#
# for image in images:
#     print(image)
#     print()
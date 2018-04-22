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

# print("******NEXT PAGE******")


output = PyPDF2.PdfFileWriter()

for index in len(reader.pages):
    page = encoder.merge(page, images)
    output.addPage(page)

outputStream = open("optimized.pdf", "wb")
output.write(outputStream)

# images2 = encoder.encode(page)
#
# # print(len(images2))
# #
# # for image in images2:
# #     print(image)
# #     print()
# output.addPage(page)

# print(len(xos))
#
# for xo in xos:
#     print(xo)
#     print()

# for img in images:
#     img_extractor.extractImages(img)


# output = PyPDF2.PdfFileWriter()
# # output.addPage(reader.getPage(0))

# for page in reader.pages:
#     encoder.merge(page, images)
#     output.addPage(page)



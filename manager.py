import PyPDF2
import encoder
import img_extractor

path = 'Impositioned.pdf'

# path = 'single_documents/publisher_1.pdf'
# path2 = 'single_documents/publisher_2.pdf'

pdf = open(path, "rb")

reader = PyPDF2.PdfFileReader(pdf)


# for page in reader.pages:
#     images = encoder.encode(page)
#     # xos = encoder.getXObjects(page)

images = encoder.encode(reader.getPage(0))

print(len(images))

for image in images:
    print(image)
    print()

# print(len(xos))
#
# for xo in xos:
#     print(xo)
#     print()

# for img in images:
#     img_extractor.extractImages(img)


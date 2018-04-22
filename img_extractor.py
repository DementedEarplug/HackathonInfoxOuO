from PIL import Image

def extractImages(image):
        if image['/Subtype'] == '/Image':
            size = (image['/Width'], image['/Height'])
            data = image.getData()
            if image['/ColorSpace'] == '/DeviceRGB':
                mode = "RGB"
            else:
                mode = "P"

            if '/Filter' in image:
                if image['/Filter'] == '/FlateDecode':
                    img = Image.frombytes(mode, size, data)
                    img.save(obj[1:] + ".png")
                elif image['/Filter'] == '/DCTDecode':
                    img = open(obj[1:] + ".jpg", "wb")
                    img.write(data)
                    img.close()
                elif image['/Filter'] == '/JPXDecode':
                    img = open(obj[1:] + ".jp2", "wb")
                    img.write(data)
                    img.close()
                elif image['/Filter'] == '/CCITTFaxDecode':
                    img = open(obj[1:] + ".tiff", "wb")
                    img.write(data)
                    img.close()
            else:
                img = Image.frombytes(mode, size, data)
                img.save(obj[1:] + ".png")
        else:
            print("No image found.")

# def extractImages(xObject):
#     for obj in xObject:
#         if xObject[obj]['/Subtype'] == '/Image':
#             size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
#             data = xObject[obj].getData()
#             if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
#                 mode = "RGB"
#             else:
#                 mode = "P"
#
#             if '/Filter' in xObject[obj]:
#                 if xObject[obj]['/Filter'] == '/FlateDecode':
#                     img = Image.frombytes(mode, size, data)
#                     img.save(obj[1:] + ".png")
#                 elif xObject[obj]['/Filter'] == '/DCTDecode':
#                     img = open(obj[1:] + ".jpg", "wb")
#                     img.write(data)
#                     img.close()
#                 elif xObject[obj]['/Filter'] == '/JPXDecode':
#                     img = open(obj[1:] + ".jp2", "wb")
#                     img.write(data)
#                     img.close()
#                 elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
#                     img = open(obj[1:] + ".tiff", "wb")
#                     img.write(data)
#                     img.close()
#             else:
#                 img = Image.frombytes(mode, size, data)
#                 img.save(obj[1:] + ".png")
#     else:
#         print("No image found.")
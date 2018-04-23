import sys
import PyPDF2
from PIL import Image

#Create an empty image list t store the refences of the images
#of page 1.
images = []

#Method to extract the images from page one and save them to images list.
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


#Method to iterate over the pdf's pages and overwrite the original images with the 
#references stored on the images list
def merge(resource, imgs):
    if '/XObject' in resource['/Resources']:
        xObject = resource['/Resources']['/XObject'].getObject()
        for xo in xObject:
            if '/Image' in xObject[xo]['/Subtype']:
                xObject[xo] = imgs.pop(0)
            elif '/Form' in xObject[xo]['/Subtype']:
                merge(xObject[xo], imgs)
    return resource

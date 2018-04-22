from PIL import Image, ImageOps
import numpy as np

image = Image.open('Im1.jpg')

image = image.convert('RGB')
image = ImageOps.invert(image)
image = image.convert('RGB')

image.save('Im1_modified.jpg')
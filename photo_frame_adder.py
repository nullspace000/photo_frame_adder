#Goal: Add frame to photos

#import image class
from PIL import Image

#load image from file
im = Image.open("image.jpg")

#use instance attributes to examine file contents
print(im.format, im.size, im.mode) PPM (512, 512) RGB

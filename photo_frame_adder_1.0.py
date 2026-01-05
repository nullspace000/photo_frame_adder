#Goal: Add frame to my photos

from PIL import Image, ImageOps

img = Image.open("image.jpg")

framed = ImageOps.expand(
    img,
    border=40,          # thickness in pixels
    fill="white"        # frame color
)

framed.save("framed.jpg")

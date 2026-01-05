from PIL import Image, ImageOps

img = Image.open("image.jpg")

# Get width and height
width, height = img.size

# Determine the longer axis
longer_axis = max(width, height)

# 10% of the longer axis (must be an int)
border_size = int(longer_axis * 0.05)

# Add white frame
framed = ImageOps.expand(
    img,
    border=border_size,
    fill="white"
)

framed.save("framed.jpg")


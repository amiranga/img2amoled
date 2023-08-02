from PIL import Image, ImageOps

file = "C:/Users/aeamu/Pictures/img.png"
img = Image.open(file)
width, height = img.size
thresh = 128
fn = lambda x: 255 if x > thresh else 0
img = img.convert("L").point(fn, mode='1')

bCount = 0
wCount = 0
for y in range(0, height):  # each pixel has coordinates
    for x in range(0, width):
        a = img.getpixel((x, y))
        if a == 255:
            wCount = wCount + 1
        else:
            bCount = bCount + 1

if wCount > bCount:
    img = ImageOps.invert(img)
img.show()

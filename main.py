from PIL import Image, ImageEnhance

file = "C:/Users/aeamu/Pictures/img1.png"
img = Image.open(file)
thresh = 150
fn = lambda x : 255 if x > thresh else 0
img2 = img.convert("L").point(fn, mode='1')
img2.show()
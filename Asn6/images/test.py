#from PIL import Image
#http://www.pythonware.com/products/pil/

import Image

im = Image.open("arch.jpg")
x = 3
y = 4

pix = im.load()
print (pix[x,y])

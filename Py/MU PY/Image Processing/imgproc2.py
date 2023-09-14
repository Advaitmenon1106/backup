import numpy as np
from PIL import Image as image

img = image.open("flowers.jpg")
img.show()
print (img.size)
img2 = img[:100][50:]
img2.show()
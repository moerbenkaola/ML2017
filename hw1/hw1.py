import numpy as np
from PIL import Image
import sys
pic1name = sys.argv[1]
pic2name = sys.argv[2]
picname = sys.argv[3]

im1 = Image.open(pic1name)
im2 = Image.open(pic2name)
im = Image.open("ans_lena.png")

im1_array = np.array(im1)
im2_array = np.array(im2)

im_array = im2_array - im1_array
im.save(picname)



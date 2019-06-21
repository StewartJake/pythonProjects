from PIL import Image
import numpy as np
import math

im = Image.open("20190616_193114.jpg")
print("Image Successfully Loaded" + '\n' + "Image Size: {0}x{1}".
        format(im.size[0], im.size[1]))

height, width = im.size
aspectRatio = height/width
# change for terminal sizes
desiredHeight =640
formulatedWidth =  math.ceil(desiredHeight/aspectRatio)

im = im.resize((desiredHeight, formulatedWidth))
print("Image Successfully Resized" + '\n' + "Image Size: {0}x{1}".
        format(im.size[0], im.size[1]))

rows, cols = im.size
px = im.load()
pxMap = np.zeros((rows,cols), dtype=tuple)
#pxMap2 = np.zeros((rows,cols), dtype=tuple)

# Pixel Object not iterable
# convert to numpy arr
for i in range(rows):
    for j in range(cols):
        pxMap[i,j] = px[i,j]

# assigns a luminosity score to each pixel
for i in range(rows):
    for j in range(cols):
        r,g,b = pxMap[i, j]
        pxMap[i,j] = (r + g + b) / 3
        #pxMap[i, j] = 0.21*r + 0.72*g +0.07*b

asciiMap = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# changes luminosity score to ascii by weights (65/256)
for i in range(rows):
    for j in range(cols):
        index = int(pxMap[i, j]*(65/256))
        pxMap[i,j] = asciiMap[index]
#        pxMap2[i, j] = (asciiMap[index],)*3

# recreate image in ascii
for i in range(rows):
    for j in range(cols):
        print(pxMap[i, j], end ="")
    print('\n', end = "")


#im2 = Image.fromarray(pxMap)
#im2.show()




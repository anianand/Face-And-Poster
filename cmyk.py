import numpy as np
import cv2
cmyk_scale = 100

def rgb_to_cmyk(r,g,b):
    if (r == 0) and (g == 0) and (b == 0):
        # black
        return 0, 0, 0, cmyk_scale

    # rgb [0,255] -> cmy [0,1]
    c = 1 - r / 255.
    m = 1 - g / 255.
    y = 1 - b / 255.

    # extract out k [0,1]
    min_cmy = min(c, m, y)
    c = (c - min_cmy) / (1 - min_cmy)
    m = (m - min_cmy) / (1 - min_cmy)
    y = (y - min_cmy) / (1 - min_cmy)
    k = min_cmy

    # rescale to the range [0,cmyk_scale]
    return np.ndarray([int(c*cmyk_scale), int(m*cmyk_scale), int(y*cmyk_scale), int(k*cmyk_scale)])
img=cv2.imread('1.jpg')
r,g,b=img[0][0]
print type(img[0][0])
print r,g,b
print rgb_to_cmyk(r,g,b) 
for row in img:
    for pixel in row:
        r,g,b=pixel
        img[row][pixel]=rgb_to_cmyk(r,g,b)
print img
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',1000,1000)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

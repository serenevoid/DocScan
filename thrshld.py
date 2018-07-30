import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Samples/transformed.png',0)
#img = cv.medianBlur(img,5)
th = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
plt.imshow(th, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
cv.imwrite('Samples/Filtered.bmp', th)

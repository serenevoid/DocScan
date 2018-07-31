# Contour
from pis import four_point_transform
import numpy as np
import rect
import cv2
import imutils
from matplotlib import pyplot as plt

image = cv2.imread('Samples/test.jpg')
image = cv2.resize(image, (3000, 2000))
edged = cv2.imread('Samples/Edged.jpg',0)

# find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
 
# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	# if our approximated contour has four points, then we
	# can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break

# mapping target points to 800x800 quadrilateral
approx = rect.rectify(screenCnt)
pts2 = np.float32([[0,0],[800,0],[800,800],[0,800]])

M = cv2.getPerspectiveTransform(approx,pts2)
dst = cv2.warpPerspective(image,M,(800,800))

cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
cv2.imwrite('transformed.png', dst) 
# show the contour (outline) of the piece of paper
cv2.drawContours(dst, [screenCnt], -1, (0, 255, 0), 2)
plt.imshow(dst, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

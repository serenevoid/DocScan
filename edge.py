#Edge detection
import cv2
from matplotlib import pyplot as plt
image=cv2.imread('Samples/test.jpg')
# choose optimal dimensions such that important content is not lost
image = cv2.resize(image, (3000, 2000))

# creating copy of original image
orig = image.copy()

# convert to grayscale and blur to smooth
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#blurred = cv2.medianBlur(gray, 5)

# apply Canny Edge Detection
edged = cv2.Canny(blurred, 0, 50)
orig_edged = edged.copy()
cv2.imwrite('Edged.jpg', edged)
#show image
plt.imshow(edged, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

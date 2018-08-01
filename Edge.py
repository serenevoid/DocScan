#Edge detection
import cv2

def Edge(list):
	for img in list:
		image=cv2.imread('Captured/{}'.format(img))
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
		cv2.imwrite('Edged/{}'.format(img), edged)

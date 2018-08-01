# Threshold
import cv2

def Threshold(list):
	for img in list:
		image = cv2.imread('Transformed/{}'.format(img),0)
		th = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
		cv2.imwrite("Thresholded/{}".format(img), th)

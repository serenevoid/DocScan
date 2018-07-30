# Video Stream from camera
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame  = cap.read()
	# Detect corners
	frame = np.float32(frame)
	corners = cv2.goodFeatureToTrack(frame, 100, 0.01, 10)
	corners = np.int0(corners)
	for corner in corners:
		x,y = corner.ravel()
		cv2.circle(frame, (x,y), 3, 255, -1)
	# Show colour image output
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		# quit when 'q' is pressed
		break
# releasing capture when finished
cap.release()
cv2.destroyAllWindows()

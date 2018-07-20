import cv2
cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	# Show colour image output
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		# quit when 'q' is pressed
		break
# releasing capture when finished
cap.release()
cv2.destroyAllWindows()

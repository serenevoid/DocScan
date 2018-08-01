from Capture import Capture
from Edge import Edge
from Transform import Transform
from Threshold import Threshold
from PDF import pdf
from pis import four_point_transform
import numpy as np
import rect
import cv2
import imutils

list = Capture()
print list
Edge(list)
Transform(list)
Threshold(list)
pdf(list)

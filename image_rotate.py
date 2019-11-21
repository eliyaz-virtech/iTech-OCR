import numpy as np
import cv2
import math
from scipy import ndimage

#img_before = cv2.imread('img3.jpg')
img_before = cv2.imread('300deg.png')
dpi=300
#img_before = cv2.resize(img_before, (640,480))
#cv2.imshow("Before", img_before)    
key = cv2.waitKey(0)

img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)
angles = []

for x1, y1, x2, y2 in lines[0]:
    cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles.append(angle)

median_angle = np.median(angles)
img_rotated = ndimage.rotate(img_before, median_angle)
rotated_90 = np.rot90(img_rotated) #rotated 90 deg once
rotated_180 = np.rot90(rotated_90)
rotated_270 = np.rot90(rotated_180)
    
print("Angle is {}".format(median_angle))



'''


import numpy as np
import cv2
import math
from scipy import ndimage


img_before = cv2.imread('img1.jpg')
#img_before = cv2.resize(img_before, (640,480))
cv2.imshow("Before", img_before)    
key = cv2.waitKey(0)

img_gray = cv2.cvtColor(img_before, cv2.COLOR_BGR2GRAY)
img_edges = cv2.Canny(img_gray, 100, 100, apertureSize=3)
lines = cv2.HoughLinesP(img_edges, 1, math.pi / 180.0, 100, minLineLength=100, maxLineGap=5)

angles = []

for x1, y1, x2, y2 in lines[0]:
    cv2.line(img_before, (x1, y1), (x2, y2), (255, 0, 0), 3)
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angles.append(angle)

median_angle = np.median(angles)
img_rotated = ndimage.rotate(img_before, median_angle)

rotated_90_clockwise = np.rot90(img_rotated) #rotated 90 deg once
rotated_180_clockwise = np.rot90(rotated_90_clockwise)
rotated_270_clockwise = np.rot90(rotated_180_clockwise)
 
#displaying all the images in different windows(optional)
cv2.imshow('median_angle_rotation', img_rotated)
# Create window with freedom of dimensions
#cv2.namedWindow("90 deg", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("90 deg", 960, 540)
cv2.imshow('90 deg', rotated_90_clockwise)
cv2.imshow('Inverted', rotated_180_clockwise)
cv2.imshow('270 deg', rotated_270_clockwise)
 
k = cv2.waitKey(0)
if (k == 27): #closes all windows if ESC is pressed
	cv2.destroyAllWindows()
    
print("Angle is {}".format(median_angle))
cv2.imwrite('rotated.jpg', img_rotated)  
'''

cv2.imwrite('output/rotated.jpg', img_rotated)  

cv2.imwrite('output/rotated_90.jpg', rotated_90)  

cv2.imwrite('output/rotated_180.jpg', rotated_180)  

cv2.imwrite('output/rotated_270.jpg', rotated_270)  

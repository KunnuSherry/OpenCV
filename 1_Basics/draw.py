import cv2 as cv
import numpy as np

blank  =np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank',blank)

# 1. Paint the image to certain color
blank[200:300, 300:400] = 0,0,255
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,100,0), thickness=-1) #frame, start, end, color, thickness
# cv.imshow('Rectangle', blank)

#3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,255,255), thickness=-1)
# cv.imshow('Circle', blank)

#4. Draw a Line
cv.line(blank, (100,250), (300,400), (255,0,255), thickness=1)
# cv.imshow('Line', blank)

#5. Write text
cv.putText(blank, "Hello My Name is Kunal", (0,250), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)


cv.waitKey(0)
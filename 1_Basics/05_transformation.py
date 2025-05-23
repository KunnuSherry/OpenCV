import cv2 as cv
import numpy as np
img = cv.imread('../Resources/images/park.jpg')

cv.imshow('Boston', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

#-x --> left, x --> right, -y --> top and y --> down

translated = translate(img, 100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv. warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45) #Postive value --> Anti Clock, Negative Value --> Clock
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0) #0-->yaxis, 1-->xaxis, -1--> both
cv.imshow('Fliped', flip)


cv.waitKey(0)
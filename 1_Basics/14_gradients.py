import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('../Resources/images/cats.jpg')
cv.imshow('cats', img)

#Laplacion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('LapLacian', lap)

#Sobel
Sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # it's the depth
Sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(Sobelx, Sobely)

cv.imshow('SobelX', Sobelx)
cv.imshow('Sobely', Sobely)
cv.imshow('Combined', combined)

#Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)
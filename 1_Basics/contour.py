import cv2 as cv
import numpy as np

img = cv.imread('../Resources/images/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

# blurred = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blurred) 

# canny = cv.Canny(blurred, 125, 175)
# cv.imshow('Canny Edges', canny)

# Another way to find edges
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)
# if pixel intensity is less than 125 it's set to black else white

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#cv.RETR_LIST--> retrun all the contours, RETR_EXT--> return external.
#contours--> all cordinates of the edges
#hierarchies--> representation to find contours

print(f'{len(contours)} contours found ! ')

#Drawing the contours on the blank image
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('CountoursDrawn', blank)

cv.waitKey(0)
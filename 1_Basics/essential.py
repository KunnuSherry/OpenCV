import cv2 as cv

img = cv.imread('../Resources/images/park.jpg')
# cv.imshow('Cat', img)

#Converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('GRAY', gray)

#blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

#edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('edges', canny)

#dilating the images
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# eroding the images
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# DILATED + ERODED = EDGE

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#Cropped
cropped = img[50:200, 50:200]
cv.imshow('s', cropped)

cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread('../Resources/images/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img) #Split the image into Blue, green and red

cv.imshow('Blue', b)
cv.imshow('red', r)
cv.imshow('Green', g)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Red', red)
cv.imshow('green', green)
cv.imshow('blue', blue)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image',merged)

cv.waitKey(0)
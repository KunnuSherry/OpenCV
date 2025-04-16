import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND --> Intersecting
And = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', And)

#Bitwise OR --> Both Intersecting and non intersecting
Or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', Or)

#Bitwise XOR --> Non Intersecting
Xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', Xor)

#Bitwise NOT --> Inverts the binary color
Not = cv.bitwise_not(rectangle)
cv.imshow('NOT', Not)
cv.waitKey(0)
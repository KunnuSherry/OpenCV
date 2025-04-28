import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('../Resources/images/cats.jpg')
cv.imshow('cats', img)

#Simple Thresholding
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Threshold Inverse', thresh)

#Adapted Thresholding : The computer get the optimised limit threshold itself
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 10)
cv.imshow('Adaptive Threshold', adaptive_thresh)

cv.waitKey(0)
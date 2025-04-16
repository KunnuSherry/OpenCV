import cv2 as cv

img = cv.imread('../Resources/images/cats.jpg')
cv.imshow('cats', img)

#Averaging
avg = cv.blur(img, (7,7)) # Higher the Kernel Size Higher the blur
cv.imshow('Average Blur', avg)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss) # Gaussian is less blurred than Average

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median) # More effecting in less blur ususally 3 kernal size

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilteral', bilateral)

cv.waitKey(0)
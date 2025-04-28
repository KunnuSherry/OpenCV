import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread('../Resources/images/cats.jpg')
cv.imshow('cats', img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('GRAY', gray)

# blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', circle)

# mask = cv.bitwise_and(img, img,  mask=circle)
# cv.imshow('Masked Image', mask)

# ## GrayScale Histogram
# gray_hist = cv.calcHist([gray], [0], circle, [256], [0,256])

# plt.figure()
# plt.title('GrayScale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


#Color Histogram
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)
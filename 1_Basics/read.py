import cv2 as cv

# The Below Program is for reading the Images in open cv

# img = cv.imread('../Resources/images/cat_large.jpg')
# cv.imshow('Cat', img)

# The Below Program is for capturing the Videos in open cv

# capture = cv.VideoCapture(0) -- For webcam
capture = cv.VideoCapture('../Resources/videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.waitKey(0)
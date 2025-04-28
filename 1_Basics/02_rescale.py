import cv2 as cv

# The Below Program is for reading the Images in open cv

# img = cv.imread('../Resources/images/cat_large.jpg')
# cv.imshow('Cat', img)

# The Below is the function to rescale the image or video
def rescaleFrame(frame, scale=0.75):
    #Can be used for all images, videos and live videos
    width = int (frame.shape[1] *scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#The Below is for changing the resoltuion, only can be used for live videos
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# The Below Program is for capturing the Videos in open cv

# capture = cv.VideoCapture(0) -- For webcam
capture = cv.VideoCapture('../Resources/videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    rescaledFrame = rescaleFrame(frame, scale=0.2)
    cv.imshow('video', rescaledFrame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.waitKey(0)
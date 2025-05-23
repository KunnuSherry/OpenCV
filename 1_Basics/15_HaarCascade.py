import cv2 as cv

# img = cv.imread('../Resources/images/lady.jpg')
# cv.imshow('Lady', img)

# gray  =cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

haar_cascade = cv.CascadeClassifier('../Resources/XML/haarFace.xml')

# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
# # Change these parameter for better results and reducing noises

# print(f'Number of faces found: {len(faces_rect)}')
# #very sensitive to noises

# #faces_rect contains the cordinates

# for(x,y,w,h) in faces_rect:
#     cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

# cv.imshow('Detected', img)

capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    gray =cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
    for(x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)   
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.waitKey(0)

cv.waitKey(0)
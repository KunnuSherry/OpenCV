import numpy as np
import os
import cv2 as cv

haar_cascade = cv.CascadeClassifier('../Resources/XML/haarFace.xml')
p=[]
for i in os.listdir(r'C:\Users\GIGABYTE\Desktop\OpenCV\Resources\Model_Train_Prac'):
    p.append(i)

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)


face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')


img = cv.imread(r'C:\Users\GIGABYTE\Desktop\OpenCV\2_FaceRecognition\testing\10915-camedia.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detact the faces first
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Lable ={p[label]} with a confidence of {confidence}')

    cv.putText(img, str(p[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Image', img)
cv.waitKey(0)
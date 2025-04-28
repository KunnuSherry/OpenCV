import os
import cv2 as cv
import numpy as np

# people = ['Virat', 'Rohit', 'Mahender']

# Other Method
p=[]
for i in os.listdir(r'C:\Users\GIGABYTE\Desktop\OpenCV\Resources\Model_Train_Prac'):
    p.append(i)

print(f'The number of people in the directory are : {len(p)}\n')

dir = r'C:\Users\GIGABYTE\Desktop\OpenCV\Resources\Model_Train_Prac' #Base Folder
haar_cascade = cv.CascadeClassifier('../Resources/XML/haarFace.xml')


features = []
labels = []
def create_train():
    for person in p:
        path = os.path.join(dir, person)
        label = p.index(person)

        for image in os.listdir(path):
            img_path = os.path.join(path, image)
            image_array = cv.imread(img_path)
            gray = cv.cvtColor(image_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # region of interest to crop
                features.append(faces_roi)
                labels.append(label)

create_train()
print(len(features))

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the recog on the deatures list and labels list
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
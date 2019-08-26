# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:09:34 2019

@author: Durgesh
"""

import numpy as np
import matplotlib.pyplot as plt
import os 
import cv2

DATADIR = "G:\di_solo_dataset"

path = os.path.join(DATADIR)
for img in os.listdir(path):
    img_array = cv2.imread(os.path.join(path,img))
    plt.imshow(img_array, cmap="gray")
    plt.show()
    break

 """img_size = 100
 new_array = cv2.resize(img_array, (img_size,img_size))
 plt.imshow(new_array,cmap = "gray")
 plt.show()
 """
img_size = 1000
new_array = cv2.resize(img_array, (img_size,img_size))
plt.imshow(new_array,cmap = "gray")
plt.show()
 
training_data = []
 
path = os.path.join(DATADIR)
for img in os.listdir(path):
    try:
        img_array = cv2.imread(os.path.join(path,img))
        new_array = cv2.resize(img_array, (img_size,img_size))
        training_data.append([new_array])
    except Exception as e:
        pass

print_len(training_data)
import random
random.shuffle(training_data) #for balancing the data for neural network unbiased prediction


#face detection by opencv

face_cascade = cv2.CascadeClassifier(r"C:\Users\Durgesh\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")    
path = os.path.join(DATADIR)
for img in os.listdir(path):
    img_array = cv2.imread(os.path.join(path,img))
    gray_img = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.35, minNeighbors =5)
    print(type(faces))
    print(faces)
    
    for x,y,w,h in faces:
        imag = cv2.rectangle(gray_img,(x,y),(x+w,y+h),(0,255,0),3)
    resized = cv2.resize(imag,(int(imag.shape[1]/7),int(imag.shape[1]/6)))
    cv2.imshow("imageface", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    break
    

test_img = cv2.imread('/file path')
faces_detected,gray_img = fr.faceDetection(test_img)
print("faces detected:", faces_detected)

for(x,y,w,h) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
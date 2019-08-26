# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:34:32 2019

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

face_cascade = cv2.CascadeClassifier(r"C:\Users\Durgesh\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")    
img_array = cv2.imread(os.path.join(path,img))
gray_img = cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.05, minNeighbors =5)

for x,y,w,h in faces:
        imag = cv2.rectangle(gray_img,(x,y),(x+w,y+h),(0,255,0),3) 
        
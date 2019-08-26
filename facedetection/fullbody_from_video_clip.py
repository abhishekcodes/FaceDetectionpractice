# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 11:00:49 2019

@author: Durgesh
"""

import cv2
import numpy as np
#import sys
import imutils
#sys.path.append(r'C:\Users\Durgesh\Anaconda3\Lib\site-packages\cv2')

cap = cv2.VideoCapture(r"G:\MOV_0723.mp4")

human_cascade = cv2.CascadeClassifier(r'C:\Users\Durgesh\Anaconda3\Lib\site-packages\cv2\data\haarcascade_fullbody.xml')

while True:
    ret,frame =cap.read()
    frame = imutils.resize(frame, width=1000, height=1000)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    human = human_cascade.detectMultiScale(gray,1.1,6)
    
    for(x,y,w,h) in human:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,23),3)
        
    cv2.imshow('video',frame)
    
    if cv2.waitKey(25) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

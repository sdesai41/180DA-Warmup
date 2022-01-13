# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:39:30 2022

@author: sohum
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:08:54 2022

@author: sohum
"""
# from geeks for geeks thresholding colors
#from stack overflow as well
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    # Threshold of blue in HSV space
    lower_blue = np.array([60, 35, 140])
    upper_blue = np.array([180, 255, 255])
     # Threshold of blue in BGR space
    lower_bluebgr = np.array([0, 0, 0])
    upper_bluebgr = np.array([255, 120, 0])
    
 
    # preparing the mask to overlay
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    maskbgr= cv2.inRange(frame, lower_bluebgr, upper_bluebgr)
   
    
    
    # The black region in the mask has the value of 0,
    # so when multiplied with original image removes all non-blue regions
    result = cv2.bitwise_and(frame, frame, mask = mask)
    
 
    #showing both rgb and hsv masks and results
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    #cv2.imshow('mask2', maskbgr)
   #cv2.imshow('result2',result2)
    cv2.imshow('result', result)
    # Our operations on the frame come here
    
    # Display the resulting frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:03:46 2020

@author: Family
"""
import cv2
import numpy as np

a = np.zeros((100,50))
b = np.ones((100,50))

img = np.uint8(255*np.concatenate((a,b),axis=1))


gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, 5)
gy = cv2.Sobel(img, cv2.CV_64F, 1, 1, 5)

mag,ang =cv2.cartToPolar(gx,gy)

gx = cv2.convertScaleAbs(gx)
gy = cv2.convertScaleAbs(gy)
mag = cv2.convertScaleAbs(mag)
ang = (180/np.pi)* ang

cv2.waitKey(0)
cv2.destroyAllWindows()






               
               
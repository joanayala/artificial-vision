# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:37:53 2020

@author: Family
"""

import cv2
import numpy as np

img_ori = cv2.imread('images/bananos.jpg')
cv2.imshow('Img-Ori', img_ori)

#Kernel's
kernel_3x3 = np.ones((3,3),np.float32)/(3*3)
output = cv2.filter2D(img_ori,-1,kernel_3x3)
#cv2.imshow('Promedio 3x3',output)

kernel_5x5 = np.ones((5,5),np.float32)/(5*5)
output = cv2.filter2D(img_ori,-1,kernel_5x5)
#cv2.imshow('Promedio 5x5',output)

kernel_31x31 = np.ones((31,31),np.float32)/(31*31)
output = cv2.filter2D(img_ori,-1,kernel_31x31)
#cv2.imshow('Promedio 31x31',output)

#Filtro Gaussiano
output = cv2.GaussianBlur(img_ori,(3,3),0) #0: Máscara automática.
cv2.imshow('Desv. Gauss 3x3', output)

output = cv2.GaussianBlur(img_ori,(11,11),0) #0: Máscara automática.
cv2.imshow('Desv. Gauss 11x11', output)

output = cv2.GaussianBlur(img_ori,(21,21),0) #0: Máscara automática.
cv2.imshow('Desv. Gauss 3x3', output)


cv2.waitKey(0)
cv2.destroyAllWindows()
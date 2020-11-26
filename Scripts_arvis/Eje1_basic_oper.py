# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:48:26 2020

@author: Family
"""

import cv2 #OpenCV
import numpy as np
import matplotlib.pyplot as plt

# :::::: ORI IMAGES ::::::
#img1 = cv2.imread('images/bananas.jpg')
#img1 = cv2.imread('images/fruta.jpg')
img1 = cv2.imread('images/lunar_cancer.jpg')

#Operaciones básicas
pxX = np.size(img1, axis=0) #W
pxY = np.size(img1, axis=1) #H
pxXY = np.size(img1, axis=None)

promManual = np.sum(img1) / (pxX * pxY * 3)

suma = np.sum(img1) #Suma
minimo = np.min(img1) #Mínimo
maximo = np.max(img1) #Máximo
prom = np.mean(img1) #Promedio
var = np.var(img1) #Varianza
de = np.sqrt(var) #Desviación estándar

#Operaciones avanzadas
#cv2.imshow('Img-Original',img1)

hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
#cv2.imshow('Img-HSV', hsv)

I = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Img-GRAY', I)

#umbral1 = 50
umbral2,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)  
binaria = np.uint8((I<umbral2)+255)
#cv2.imshow('Img-Binary', binaria)

#Histograma
data = I.flatten()
red = img1[:,:,0].flatten()
green = img1[:,:,1].flatten()
blue = img1[:,:,2].flatten()

plt.hist(data,bins=100)
plt.hist(red, bins=1000, histtype="stepfilled", color="red")
plt.hist(green, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue, bins=1000, histtype="stepfilled", color="blue")

cv2.waitKey(0)
cv2.destroyAllWindows()
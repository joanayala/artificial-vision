# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:48:26 2020

@author: Family
"""

import cv2 #OpenCV
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('images/bananas.jpg')
#cv2.imshow(':::Image :::', img1) #Image read

pxX = np.size(img1, axis=0) #W
pxY = np.size(img1, axis=1) #H
pxXY = np.size(img1, axis=None)

#promManual = np.sum(img1) / (pxX * pxY)

suma = np.sum(img1)
minimo = np.min(img1)
maximo = np.max(img1)
prom = np.mean(img1)


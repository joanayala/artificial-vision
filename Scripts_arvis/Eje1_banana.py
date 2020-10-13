# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:02:23 2020

@author: Family
"""

import numpy as np
import cv2
import matplotlib as plt

img = cv2.imread('images/bananas.jpg')

I = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
umbral = 245
binary = np.uint8((I<200)*255)

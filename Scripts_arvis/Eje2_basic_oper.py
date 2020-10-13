# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:39:51 2020

@author: Family
"""

#Developer: Joan C. Ayala

''' 
Glossary:
    CV2 Functions/methods
      ->cv2 => OpenCV
      ->imread => image(s) read
      ->add => add images (addition)
      ->imshow => show the image(s)
      
Script description:
    1. Download 2 different images.
    2. Apply basic math operations.
     -> Add two images.
     -> Subst two images.
'''

#Import library (ies)
import cv2

#def add_images(x, y):
#    #Here the images are added.
#    new_image = cv2.add(x, y)
#    cv2.imshow('New image', new_image)
    
    
#Main :::::::::::::::::::::::::::::
img_1 = cv2.imread('images/car1.jpg')
img_2 = cv2.imread('images/car1.jpg')

new_image = cv2.add(img_1, img_2)
cv2.imshow('New image', new_image)

#add_images(img_1, img_2)

cv2.waitKey(0)
cv2.destroyAllWindows()









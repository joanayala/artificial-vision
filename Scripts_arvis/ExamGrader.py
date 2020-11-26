# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:03:05 2020

@author: Family
Proyect 1: Exam Grader
Developer: Joan C. Ayala
"""
'''
Glosary:
    dilate => 
    drawContours =>
    RETR_TREE => 
    thickness =>
    CHAIN_APPROX_SIMPLE =>
    (...,-1,...) =>
'''


#Libraries OpenCV, Numpy
import cv2
import numpy as np

#0. Load images
#imaExam = cv2.imread('images/ExamGrader/Cal_1.jpg',0)
imaExam = cv2.imread('images/ExamGrader/Cal_2.jpg',0)
#imaExam = cv2.imread('images/ExamGrader/Cal_3.jpg',0)

#1. Canny
can = cv2.Canny(imaExam,20,150)
kernel = np.ones((5,5),np.uint8)
bordes = cv2.dilate(can, kernel)

#Obtener contornos
contour,_ = cv2.findContours(
    bordes, 
    cv2.RETR_TREE, 
    cv2.CHAIN_APPROX_SIMPLE) #Sacar los contornos

#Dibujar contornos
objects = bordes.copy()
cv2.drawContours(
    objects,
    [max(contour, key=cv2.contourArea)],-1,255,thickness=-1)

#Get labels
output = cv2.connectedComponentsWithStats(objects,4,cv2.CV_32S)
cantObj = output[0] # Objects quantity
labels = output[1] # Labels
stats = output[2] #stats

#Get ArgMax
mask = np.uint8(255*(np.argmax(stats[:,4][1:])+1==labels))

contours,_ = cv2.findContours(
    mask, 
    cv2.RETR_TREE, 
    cv2.CHAIN_APPROX_SIMPLE) #Sacar los contornos
cnt = contours[0] # Puntos específicos

#ConvexHull => Polígono convexo
hull = cv2.convexHull(cnt) # Obtener puntos del polígono que se está creando
puntoConvex = hull[:,0,:] # Generar el punto convexo
m,n = mask.shape # Genero Dimensiones de la imagen
ar = np.zeros((m,n)) #Crear matriz de ceros
mascara_convex = np.uint8(
    cv2.fillConvexPoly(ar,puntoConvex,1)) # 1: Grosor de línea

#cv2.imshow('Exam - Source',imaExam)

cv2.waitKey(0)
cv2.destroyAllWindows()
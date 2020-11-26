# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:29:22 2020

@author: Family
"""

import cv2
import numpy as np
from scipy import ndimage

img1 = cv2.imread('images/bananos.jpg') #Ori image
#img1 = cv2.imread('images/A.jpg') #Ori image
#img1 = cv2.imread('images/B.jpg') #Ori image
#img1 = cv2.imread('images/car1.jpg') #Ori image
#img1 = cv2.imread('images/car3.jpg') #Ori image
#img1 = cv2.imread('images/lunar_cancer.jpg') #Ori image
I = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY) #Gray image
umbral,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU) #Get umbral
mascara = np.uint8((I<umbral)*255) #Binary image

#cv2.imshow("Img-COLOR-ori",img1)
#cv2.imshow("Img-GRAY",I)
#cv2.imshow("Img-BINARY",mascara)

#Get labels
output = cv2.connectedComponentsWithStats(mascara,4,cv2.CV_32S)
cantObj = output[0] # Objects quantity
labels = output[1] # Labels
stats = output[2]

#Get ArgMax
mascara_limpia = (np.argmax(stats[:,4][1:])+1==labels)
              
#Rellenar huecos de la nueva máscara
#Esto nos permite a futuro obtener valores como el área, perímetro, etc.
new_mascara = ndimage.binary_fill_holes(mascara_limpia).astype(int)

#Medición del área y perímetro en la imágen.
last_mascara = np.uint8(new_mascara*255)
contours,_ = cv2.findContours(last_mascara, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Sacar los contornos
cnt = contours[0] # Puntos específicos
Perimetro = cv2.arcLength(cnt, False)

#Area_man = np.sum(last_mascara/255)
Area = cv2.contourArea(cnt)

#ConvexHull => Polígono convexo
hull = cv2.convexHull(cnt) # Obtener puntos del polígono que se está creando
puntoConvex = hull[:,0,:] # Generar el punto convexo
m,n = last_mascara.shape # Genero Dimensiones de la imagen
ar = np.zeros((m,n))
mascara_convex = np.uint8(cv2.fillConvexPoly(ar,puntoConvex,1)) # 1: Grosor de línea

#BoundingBox
#=>BoundingBox => Rotado (ángulos)
rect = cv2.minAreaRect(cnt)
box = np.int0(cv2.boxPoints(rect))
m,n = mascara_convex.shape
ar = np.zeros((m,n))
mascara_rectang = np.uint8(cv2.fillConvexPoly(ar,box,1))

#=>BoundingBox Recto =>
x, y, w, h = cv2.boundingRect(cnt)
#ractangle(img_ori, vertices, ancho y alto, color de línea, grosor de línea)
cv2.rectangle(img1, (x,y), (x+w, y+h), (255,0,0) , 1)


contours,_ = cv2.findContours(mascara_convex, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Sacar los contornos
cv2.drawContours(img1, contours, -1, (0,255,0), 1)

contours,_ = cv2.findContours(mascara_rectang, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Sacar los contornos
cv2.drawContours(img1, contours, -1, (0,0,255), 1)

cv2.imshow("Img-COLOR-Bounding",img1)

#Segmentar el objeto de interés => Aislar el fondo del objeto a procesar.

segmentoColor = np.zeros((m,n,3)).astype(np.uint8)

#Color
segmentoColor[:,:,0] = np.uint8(img1[:,:,0]*new_mascara)
segmentoColor[:,:,1] = np.uint8(img1[:,:,1]*new_mascara)
segmentoColor[:,:,2] = np.uint8(img1[:,:,2]*new_mascara)
#gray
segmentoGray = np.zeros((m,n))
segmentoGray[:,:] = np.uint8(I*new_mascara)

cv2.imshow('Img-segmento-color', segmentoColor)
cv2.imshow('Img-segmento-gray', segmentoGray)


cv2.waitKey(0)
cv2.destroyAllWindows()
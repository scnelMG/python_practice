# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 11:15:41 2021

@author: 박민규
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# import image
im = cv.imread('son_pic.jpg')

# BGR
plt.figure()
plt.title('Original')
plt.imshow(im)

# RGB
rgb = cv.cvtColor(im,cv.COLOR_BGR2RGB)
plt.figure()
plt.imshow(rgb)
plt.title('RGB')

# gray scale
gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title('Gray')

# blur
blur = cv.blur(im,(20,100))
blur1 = cv.cvtColor(blur,cv.COLOR_BGR2RGB)
plt.subplot(121)
plt.imshow(rgb)
plt.title('RGB')
plt.subplot(122)
plt.imshow(blur1)
plt.title('Blur')

#blur2 = cv.cvtColor(im,cv.COLOR_BGR2RGB)
#plt.imshow(blur2)
#blur = cv.blur(blur2,(50,50))
#plt.imshow(blur)

# edge detaction
edges = cv.Canny(gray,0,200)
plt.subplot(121)
plt.imshow(gray,cmap='gray')
plt.title('Gray')
plt.subplot(122)
plt.imshow(edges,cmap='gray')
plt.title('Edge Detaction')









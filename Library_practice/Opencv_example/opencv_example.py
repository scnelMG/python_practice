# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 02:09:47 2021

@author: 박민규
"""

# import libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# lead image
img = cv.imread('son_pic.jpg')
plt.imshow(img)

# convert RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)

# convert to grayscale to Face recognition
gray = cv.cvtColor(rgb,cv.COLOR_RGB2GRAY)
plt.imshow(gray, cmap='gray')

# face detection
classfier = cv.CascadeClassifier(
    '.\\haarcascades\\haarcascade_frontalface_default.xml')

rects = classfier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5) # 사각형으로 표시됨

print('Faces found: {}'.format(len(rects)))

# rectangle
x,y,w,h = rects[0] # x값,y값,넓이, 높이

# drew a rectangle
cv.rectangle(rgb,(x,y),(x+w,y+h),(0,255,0),3) #(그릴 대상 사진, 시작점, 끝점, 색상, 선 굵기)

# image plot
plt.imshow(rgb)
# %% several face recognition

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# lead image
img = cv.imread('spurs_pic.jpg')
plt.imshow(img)

# convert RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)

# convert to grayscale to Face recognition
gray = cv.cvtColor(rgb,cv.COLOR_RGB2GRAY)
plt.imshow(gray, cmap='gray')

# face detection
classfier = cv.CascadeClassifier(
    '.\\haarcascades\\haarcascade_frontalface_default.xml')

rects = classfier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5) # 사각형으로 표시됨

print('Faces found: {}'.format(len(rects)))

# rectangle 여러명일때 변화되는 부분
# x,y,w,h = rects[0] # x값,y값,넓이, 높이
for (x,y,w,h) in rects:
    cv.rectangle(rgb,(x,y),(x+w,y+h),(0,255,0),)
# drew a rectangle
#cv.rectangle(rgb,(x,y),(x+w,y+h),(0,255,0),3) #(그릴 대상 사진, 시작점, 끝점, 색상, 선 굵기)

# image plot
plt.imshow(rgb)

# save pic
bgr = cv.cvtColor(rgb,cv.COLOR_RGB2BGR)
cv.imwrite('spurs_pic_faces2.jpg',bgr)







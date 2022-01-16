# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 13:14:59 2021

@author: 박민규
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

M = np.zeros((2,3)) #tuple로 제공해야함
M = np.ones((2,3)) 

# image size variables
Height = 4
Width = 5
Depth = 3

#black
M = np.zeros((Height, Width, Depth))
plt.imshow(M)
plt.grid()
#red
M[:,:,0]= 255
plt.imshow(M)
plt.grid()
#green
M = np.zeros((Height, Width, Depth))
M[:,:,1]= 0
plt.imshow(M)
plt.grid()
#blue
M = np.zeros((Height, Width, Depth))
M[:,:,2]= 255
plt.imshow(M)
plt.grid()
# white
M = np.ones((Height, Width, Depth))*255
plt.imshow(M)
plt.grid()
#black
M = np.ones((Height, Width, Depth))*0
plt.imshow(M)
plt.grid()
#부분만 원하는 색
#white
M[0,0,:]=255
plt.imshow(M)
plt.grid(False)
#green
M[0,0,0]=0
M[0,0,1]=255
M[0,0,2]=0
plt.imshow(M)
plt.grid(False) 
#red
M[0,0,0]=255
M[0,0,1]=0
M[0,0,2]=0
plt.imshow(M)
plt.grid(False) 
#blue  
M[0,0,0]=0
M[0,0,1]=0
M[0,0,2]=255
plt.imshow(M)
plt.grid(False)  
#black
M[0,0,0]=0
M[0,0,1]=0
M[0,0,2]=0
plt.imshow(M)
plt.grid(False)   
#세로줄만 원하는 색
M[:,0,1]=255
plt.imshow(M)
plt.grid(False) 

M[:,3,2]=255 
plt.imshow(M)
plt.grid(False)  
#가로줄
M[3,:,2]=255 
M[3,:,1]=0
M[3,:,0]=0
plt.imshow(M)
plt.grid(False) 

M[1,:,2]=0 
M[1,:,1]=255
M[1,:,0]=255
plt.imshow(M)
plt.grid(False) 

# 그림 두배로 늘리기-세로
M_vt = np.vstack([M,M])
plt.imshow(M_vt)
# 그림 두배로 늘리기-가로
M_hz = np.hstack([M,M])
plt.imshow(M_hz)
# 이미지 어둡게
M_hz = (M_hz/255)*0.5
plt.imshow(M_hz)

# checkerboard image
M = np.zeros((5,5,3))
plt.imshow(M)

# turn into white
M[:,:,:]= 1
plt.imshow(M)

M = np.zeros((5,5,3))
M[:]=1
plt.imshow(M)

# checkerboard
M = np.zeros((5,5,3))
plt.imshow(M)
M[0::2,0::2,:]=1
plt.imshow(M)
M[1::2,1::2,:]=1
plt.imshow(M)

N = M.copy()

# change white to gray
idx = np.where(N==1)
N[idx] = 0.5
plt.imshow(N)

# change black to white
idx = np.where(N==0)
N[idx] = 1
plt.imshow(N)

# copy again
N = M.copy()
plt.imshow(N)

# color inverse
idx_w = np.where(N==1)
idx_b = np.where(N==0)
N[idx_w]=0
N[idx_b]=1
plt.imshow(N)

# change white to green
idx1 = np.where(N==1)
N[idx1[0],idx1[1],0] = 0
N[idx1[0],idx1[1],2] = 0
plt.imshow(N)

# change black to red
flag_r = (N[:,:,0]==0)
flag_g = (N[:,:,1]==0)
flag_b = (N[:,:,2]==0)

flag_blk = flag_r & flag_g &flag_b
idx_blk = np.where(flag_blk == True)

N[idx_blk[0],idx_blk[1], 0] =1
plt.imshow(N)

# change black to red (another way)
N = M.copy()
plt.imshow(N)

N_sum = np.sum(N, axis=2)
idx_blk = np.where(N_sum == 0)
N[idx_blk[0],idx_blk[1], 0] =1
plt.imshow(N)

# change diagonal to green
np.fill_diagonal(N[:,:,0],0)
np.fill_diagonal(N[:,:,1],1)
np.fill_diagonal(N[:,:,2],0)
plt.imshow(N)

# jet scale  
M = np.linspace(0,1,10)
M = M[:,np.newaxis]
M = np.repeat(M,10,axis=1)
plt.imshow(M,cmap='jet')

# transpose
M_tr = np.transpose(M)
plt.imshow(M_tr,cmap='gray')





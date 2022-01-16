# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 00:58:51 2021

@author: 박민규
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.interpolate as interp
import gzip
import pickle as pkl

# load data
file = gzip.GzipFile('GlobalTemperatureData.pkl.gz','rb')
df = pkl.load(file)
file.close

df.keys()

YR = list(df.keys())
print(YR)

iyr = 0
df_yr = df[YR[iyr]]

df_yr.keys()

df_yr

data = df_yr[['lon','lat','Temperature(i,j)']].to_numpy()
len(data[:,0])

data[np.where(data>999)] = np.nan
data

# grid
x = np.linspace(-180,180,100)
y = np.linspace(-90,90,100)
grid_x, grid_y = np.meshgrid(x,y)
np.shape(grid_x)
print(grid_x)
np.shape(grid_x)
print(grid_x)
data_interp = interp.griddata(data[:,[0,1]],data[:,2],(grid_x, grid_y), method= 'linear')

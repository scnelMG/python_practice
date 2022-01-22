# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 19:00:40 2021

@author: 박민규
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x= np.array(np.arange(1,6,1))
y= np.array([1.,0.8,0.4,0.3,0.2])
x
# plot
plt.plot(x,y,'*')

# linear interpolation
f_lin = interpolate.interp1d(x, y)
x_new = np.arange(1,5,0.1)
y_lin = f_lin(x_new)

# splint interpolation
tck = interpolate.splrep(x,y,s=0)
y_spl = interpolate.splev(x_new, tck,der=0)

# plot
fig, ax = plt.subplots()
ax.plot(x,y,'o',label='Data')
ax.plot(x_new, y_lin, label='Linear')
ax.plot(x_new, y_spl, label='Spline')
ax.legend()







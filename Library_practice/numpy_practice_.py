
import numpy
a = numpy.arange(10)
a

a = numpy.array([10, 20, 30])
a

import numpy as np
a = np.array([10, 20, 30])
a

# size related variables
a

a.shape
a.ndim
a.dtype
a.itemsize
a.size
type(a)

# number types
a= np.array([10,20, 30])
a.dtype

a[2] =30.1
a.dtype
a

a.dtype.name
a= a.astype('float64')
a[2] =30.1
a
a.dtype

b = np.array([10., 20., 30.])
b.dtype

c = np.array([10.1,20.1,30.9], 'int32')
c

# divide by 2
x = np.array([7, 9, 11])
y= x/2
y
x.dtype
y.dtype

# int32 vs int64
x = np.array([0])
x[0] = 2147483647

x[0] = x[0] + 1
x = np.array([0], 'int64')
x[0] = 2147483647

x[0] = x[0] + 1
x

x[0]= 9223372036854775807
x[0] = x[0] + 1

# make 1D array
x = np.array([10.,20.])

a = np.array(10,20,30)
a = np.array([10, 20, 30])
a = np.array({10, 20, 30})
a = np.array([10,'abc', 30])
2*a

a = np.array([10.,20.,30.])
a
# make 2D array
a= np.array([ [10,20,30],[40,50,60]])
a
a.shape
a.itemsize
a.dtype
a.size

a= np.array([ [10,20,30],[40,50,60],[70,80,90]])
a.shape
# make 3D array
a= np.array(
    [
     [[10,50],[20,60]],
     [[30,70],[40,80]]
     ]
    )
a.ndim
a.shape

# complex number
a = np.array([10+10j, 20+20j])
a.dtype
a = np.array([10, 20], 'complex')

# matrix
a = np.array([10,20])
a.shape
b = np.matrix([10,20])
b.shape
b= np.matrix([[10,20],[30,40]])
b.shape
b= np.matrix([[[3]]])

# insert
a = np.array([10,20,30])
a = np.insert(a,0,5)
a
# delete
a = np.delete(a,0)
a

# Array Generation Functions
a = np.array([1,2,3])

a = np.arange(4)
a = np.zeros((2,3))
a
a.shape
a = np.ones((2,3))

a = np.linspace(0,5,6)

a = np.logspace(0,5,11)

# Basic Operations
a = np.array([10,20,30])
b = np.array([1,2,3])
c= a+b

c = b**2
c = 2*a
idx = b < 20
idx = a < 20

a = a + 1
a *=2

a = np.array([10,20,30])
b = np.array([1.,2.,3.])
a += b

a = np.array([10,20,30])
b = np.array([1,2,3])

np.add(a,b)
np.subtract(a,b)
np.multiply(a,b)
np.divmod(a,b)
np.exp(b)
np.sqrt(b)

import numpy as np
a = np.array([10, 20, 30])
np.mean(a)
a.mean()

np.average(a) # 가중치 줄수 있음
np.average(a, weights = [1,1,1])
np.average(a, weights = [1,1,0])

np.median(a)
np.cumsum(a)
np.cov(a)
s= np.std(a)
s**2 
np.var(a)

x = np.array([10,20,30])
y = x.sum()

x = np.array([10.,20.,30.,25.,15.])
x.min()
x.argmin()
x_min, x_min_index = x.min(), x.argmin()

x.max()
x.argmax()

x.ptp() #최대값과 최소값의 차이

x.sort()

x = np.array([10.,20.,30.,25.,15.])
y = np.sort(x)
idx = np.argsort(x) #sort전 index 표시
y = x[idx]

a = np.array([10,20,30])
b = np.array([-5,25])
np.searchsorted(a,b)

d = np.arange(1,7,1)

d.reshape(2,3) #1차원 2개 2차원 3개
e = d.reshape(3,2)

f =np.linspace(1,10,10) #1부터 10까지 10개로 나눔

g =np.linspace(1,10,10).reshape(2,5)

a = np.array([[1,2],[3,4]])

np.repeat(a,2)
np.repeat(a,2,axis=0)
np.repeat(a,2,axis=1)
np.repeat(a,2,axis=2)

np.repeat(a,[1,2],axis=0)
np.repeat(a,[3,2],axis=0)

np.repeat(a,[1,2],axis=1)
np.repeat(a,[3,2],axis=1)

a= np.array([[1],[2],[3]])
b= np.array([[4],[5],[6]])
np.concatenate((a,b), axis=0)
np.concatenate((a,b), axis=1)
np.concatenate((a,b), axis=2)

a= np.array([10,20,30])
b= np.array([40,50,60])
np.vstack((a,b)) #세로
np.hstack((a,b)) #가로

A = np.array([[10,20,30],[40,50,60]])

np.hsplit(A,2)
np.hsplit(A,3)

b= np.vsplit(A,2)
np.vsplit(A,3)
type(b)
type(b[0])

A = np.array([[10,20,30],[40,50,60]])
A.transpose()

A.ravel()
A.reshape(-1)
A.ravel(order='C') #C-style: row major
A.ravel(order='F') #Fortran-style: column-major
A.flatten()

A = np.array([[1,2,3]])
B = A.squeeze()
A.shape
B.shape

A = np.array( [[[1,2]], [[3,4]], [[4,5]] ])

B = A.squeeze()

# [1,2,3] and [4,5,6]
# => [1,4]
#    [2,5]
#    [3,6]
# idea 1
A1 = np.array([1,2,3])
B1 = np.array([4,5,6])

A2 = A1[:,np.newaxis]
B2 = B1[:,np.newaxis]

np.concatenate((A2,B2), axis=0)
C= np.concatenate((A2,B2), axis=1)

# idea 2
C = np.vstack((A1,B1)).transpose()

# idea 3
C = np.hstack((A1,B1)).reshape(2,3).transpose()

A = np.array([10,20,30])
B = A
B[0] = 99

import numpy as np
B is A
id(A)
id(B)

# shallow copy
A = np.array([10,20,30,40])
B = A.view()

B is A
id(A)
id(B)
B[0]=99

B.shape = (2,2)
B[0][1]
B[0][1]=7
A.shape

# deep copy
A = np.array([10,20,30,40])
B = A.copy()
B[0] = 99
B is A
B.base is A
B.flags.owndata

# logic funciton
import  numpy as np

a = np.array([0,1,2])
a.all()
a.any()
a.nonzero()

b = a.nonzero()

np.where(a>0)
a = np.array([0,10,20])
np.where(a>0)
a = np.array([30,0,20])
np.where(a>0)

np.where(a==0)

# indexing & slicing

M1 = np.array([100, 101, 102, 103, 104])
M1[0]
M1[[2,3]]
M1[2:5]
M1[::1]
M1[::2]
M1[::-1]
M1[-2::-1]
M1[-2::-2]

M2 = np.array([ [100,101,102], [200,201,202]])
M2[1][1]
M2[0,1]
M2[:,0]
Y = M2[:,0]
Y.shape
Y = Y[:,np.newaxis]
Y.shape
Y.shape = (1,2)

M3 = np.array([ [ [100,101,102,103],
                 [104,105,106,107],
                 [108,109,110,111]]
               ,[ [200,201,202,203], [204,205,206,207],
                 [208,209,210,211]]])


x = np.array([10,20,30])
idx = np.where(x==30)
x[idx]

idx = (x==30)
x[np.where(x==30)]
x[np.nonzero(x==30)]

# image
image = np.array([[255,0,255],[255,0,255],[255,0,255]])

idx = np.where(image == 255)
image[idx] =0

# linear algebra
M = np.array([[10,20],[30,40]])
N = np.array([[1,2],[3,4]])
M * N
M @ N
M.dot(N)

a = np.zeros((3,3))
b = np.ones((3,3))

c= np.trace(b)

# M@x = y
M = np.array([[1,2],[3,4]])

y = np.array([[1],[3]])

M_inv = np.linalg.inv(M)

x = M_inv@y

np.linalg.solve(M, y)

np.linalg.eig(M)

# singular value decomposition
np.linalg.svd(M)

N = np.zeros((5,5))
np.fill_diagonal(N, 100)

# numpy example

A = np.array([ [10,20,30],[40,50,60],[70,80,90]])
B = np.array([[1],[2],[3]])
B = B.repeat(3,axis=1)
A*B

# broadcasting
A = np.array([ [10,20,30],[40,50,60],[70,80,90]])
B = np.array([[1],[2],[3]])
A*B

# function usage example
def f(x,y):
    return x*y
b= np.fromfunction(f,(5,4),dtype=int)

a = np.array([10,20,30,40,50])
b = np.array([30,50])
np.setdiff1d(a,b)

x = np.random.randint(100)
x = np.random.rand(5)*100
































































#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 20:57:35 2017

@author: xogoss
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:26:11 2017

@author: xogoss
"""

from skimage.io import imread
import numpy as np
from matplotlib import pyplot  
import scipy as sp  
import numpy as np  
from sklearn import svm  
import matplotlib.pyplot as plt  
from sklearn.cluster   import KMeans  
from scipy import sparse  
import math

image = imread('777min.png', as_grey=True)
imageRGB = imread("777min.png")#,as_grey = True)

row = len(image)
col = int(image.size/row)

print(type(image))
pyplot.imshow(image, interpolation='nearest')
pyplot.show()

yy = int(math.sqrt(1000*col/row))
xx = int(1000/yy)

#compress =[[0]*806]*506
x = [[0 for i in range(yy)] for i in range(xx)]
xRGB = [[[0 for i in range(2)] for i in range(yy)] for i in range(xx)]
#compress = np.array(compress)
c_row = int(row/xx)
c_col = int(col/yy)

for i in range(0,xx):
    for j in range(0,yy):
        x[i][j] = image[i*c_row][j*c_col]
        xRGB[i][j] = imageRGB[i*c_row][j*c_col]

x = np.array(x)
xRGB = np.array(xRGB)
#==============================================
dec = np.around(x, decimals=2)
nUser = dec.shape[0]
x = dec.flatten()
print(dec.flatten())

pyplot.imshow(imageRGB, interpolation='nearest')
pyplot.show()
#-----------using KMeans cluster------------------#
num_clusters = 2
clf = KMeans(n_clusters=num_clusters)  #n_init=1, verbose=1)  
clf.fit(x.reshape(-1,1))
lable = clf.labels_
#print(clf.labels_)

#-----------calculate ai&bi----------------------#
center1 = np.around(clf.cluster_centers_[0][0],decimals = 5)
center2 = np.around(clf.cluster_centers_[1][0],decimals = 5)
print(center1)
print(center2)
ai = (x-center1)*(x-center1)
bi = (x-center2)*(x-center2)
print(ai)
print('----------------------------')
print(bi)

#-----------------print image-------------------#
matlable = lable.reshape(xx,yy,1)
zero = [[[0 for i in range(2)]for i in range(yy)] for i in range(xx)]
matlable1 = np.concatenate((matlable,zero), axis=2)

for i in range(len(matlable)):
    for j in range(int(matlable.size/len(matlable))):
        #print("!",matlable[i][j])
        if (matlable[i][j][0] == 1):
            #flag = matlable[i][j].pop(0)
            #matlable[i][j] = [0 for i in range(3)]
            matlable1[i][j][0] = xRGB[i][j][0]
            matlable1[i][j][1] = xRGB[i][j][1]
            matlable1[i][j][2] = xRGB[i][j][2]
        else:
            #flag = matlable[i][j].pop(0)
            #matlable[i][j] = [0 for i in range(3)]
            matlable1[i][j][0] = 255
            matlable1[i][j][1] = 255
            matlable1[i][j][2] = 255
            #matlable[i][j] = [0 for i in range(3)]
            #matlable[i][j] = np.array([255,255,255])
print(matlable.size)

matlable2 = matlable1.astype(np.uint8)

pyplot.imshow(matlable2, interpolation='nearest')
pyplot.show() 

#-----------------network flow-----------------#
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

#file = input()
image = imread("777.png", as_grey=True)
dec = np.around(image, decimals=2)
nUser = dec.shape[0]
x = dec.flatten()
print(dec.flatten())
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
matlable = lable.reshape(506,806)
pyplot.imshow(matlable, interpolation='nearest')
pyplot.show() 

#-----------------network flow-----------------#

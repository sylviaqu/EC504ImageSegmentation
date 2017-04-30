# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:14:39 2017

@author: wqmj
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 16:11:46 2017

@author: wqmj
"""

from tkinter import *
from PIL import Image
from PIL import ImageTk
import numpy as np
from skimage.io import imread
import numpy as np
from matplotlib import pyplot  
import scipy as sp  
from sklearn import svm  
import matplotlib.pyplot as plt  
from sklearn.cluster   import KMeans  
from scipy import sparse  
import time
from collections import defaultdict
  
#This class represents a directed graph using adjacency matrix representation

path = "erhan.jpeg"
a = []
print(type(a))
flag = 0
#---------------------------------------------------------------#

def seg():  
    
    global path
    global flag
    flag = 0
    print("seg begin")
    imageRGB = imread(path)#,as_grey = True)
    image = imread(path,as_grey = True)
    
    global row
    global col
    row = len(image)
    col = int(image.size/row)
    
    dec = np.around(image, decimals=2)
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

#-----------calculate ai&bi----------------------#
    center1 = np.around(clf.cluster_centers_[0][0],decimals = 5)
    center2 = np.around(clf.cluster_centers_[1][0],decimals = 5)
    print(center1)
    print(center2)
    ai = (x-center1)*(x-center1)
    bi = (x-center2)*(x-center2)

#-----------------print image-------------------#
    print(a[0],a[1])
    
        
    matlable = lable.reshape(row,col,1)
    if matlable[a[1]][a[0]][0] == 1:
        fff = 1
    else:
        fff = 0
        
    zero = [[[0 for i in range(2)]for i in range(col)] for i in range(row)]
    matlable1 = np.concatenate((matlable,zero), axis=2)
    
    for i in range(len(matlable)):
        for j in range(int(matlable.size/len(matlable))):
            if (matlable[i][j][0] == fff):
                matlable1[i][j][0] = imageRGB[i][j][0]
                matlable1[i][j][1] = imageRGB[i][j][1]
                matlable1[i][j][2] = imageRGB[i][j][2]
            else:
                matlable1[i][j][0] = 255
                matlable1[i][j][1] = 255
                matlable1[i][j][2] = 255
    
    matlable2 = matlable1.astype(np.uint8)
   
    img = Image.fromarray(matlable2,'RGB')
    img.save('after.png')
    print("seg end")
    #label.config(image = photo2)
    flag = 1
    print("flag =====",flag)
    updateimage()
    
    print("seg end end")
    #print(type(matlable2))


#--------------------------------------------------------------------------#   
def leftClick(event):
    global a
    a = [0,0]
    a[0] = event.x
    a[1] = event.y
    #print(a)
    seg()
    
    return (event.x,event.y)
    
    
def updateimage():
    global flag
    global root
    if flag == 1:
        print("flag =", flag)
        #while(Image.open("after.png") is False):
        #    pass
        time.sleep(5)
        #root = Toplevel()
        photo2 = ImageTk.PhotoImage(file = "after.png")
        label.config(image = photo2)
        root.mainloop()
        
        

if __name__=="__main__":
    global root
    root = Tk()
    root.title("Xiaolizi~")
    global path
    #photo = ImageTk.PhotoImage(file = "777.png")
    photo1 = ImageTk.PhotoImage(file = path)
    photo1 = np.array(photo1)
   
    #print(type(photo))
    global label
    label = Label(root,image = photo1)
    
    label.bind("<Button-1>",leftClick)
    label.pack()
    print("1")
    #photo2 = ImageTk.PhotoImage(file = "erhan.jpeg")
    
    root.mainloop()

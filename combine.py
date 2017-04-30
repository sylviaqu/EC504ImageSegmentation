#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:08:08 2017

@author: xogoss
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 20:56:00 2017

@author: wqmj
"""

# Python program for implementation of Ford Fulkerson algorithm
  
from collections import defaultdict
  
#This class represents a directed graph using adjacency matrix representation
class Graph:
  
    def __init__(self,graph):
        self.graph = graph # residual graph
        self. ROW = len(graph)#length of graph = 202
        #self.COL = len(gr[0])
         
  
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
    def BFS(self,s, t, parent):
        
        # Mark all the vertices as not visited
        visited =[False]*(self.ROW)
        print("length of visited = ", len(visited))
         
        # Create a queue for BFS
        queue=[]
         
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
         
        # Standard BFS Loop
        while queue:
            
            #Dequeue a vertex from queue and print it
            u = queue.pop(0)
            #print("u = ", u)
            #print("graph[u] = ", self.graph[u])
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    
                    print("parent = ", parent)
                    print("queue = ",queue)
                    print("visited = ", visited)
            print("-----------------------------------")
        # If we reached sink in BFS starting from source, then return
        # true, else false
        print("queue is empty")
        print(True if visited[t] else False)
        print("====================================================")
        return True if visited[t] else False
             
     
    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
        print("into fordfulkerson.")
        # This array is filled by BFS and to store path
        parent = [-1]*(self.ROW)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")#无穷
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]
 
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
"""
#This code is contributed by Neelam Yadav
"""
import numpy as np
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

#---------------read image---------------------------------#
image = imread('777min.png', as_grey=True)
imageRGB = imread("777min.png")#,as_grey = True)

#print(Reimage.size)
#print(Reimage)
#----------------compress image----------------------------#
row = len(image)
col = int(image.size/row)

print(type(image))
pyplot.imshow(image, interpolation='nearest')
pyplot.show()

yy = int(math.sqrt(1000*col/row))
xx = int(1000/yy)

#compress =[[0]*806]*506
image1 = [[0 for i in range(yy)] for i in range(xx)]
image1RGB = [[[0 for i in range(2)] for i in range(yy)] for i in range(xx)]
#compress = np.array(compress)
c_row = int(row/xx)
c_col = int(col/yy)

for x1 in range(0,xx):
    for y1 in range(0,yy):
        image1[x1][y1] = image[x1*c_row][y1*c_col]
        image1RGB[x1][y1] = imageRGB[x1*c_row][y1*c_col]

image1 = np.array(image1)
image1RGB = np.array(image1RGB)

x = np.resize(image1,(1,xx*yy))
x = x[0]
#----------------K-Means----------------------------------#
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


#-----------------build graph------------------------------#
bpgraph = [[0 for x in range(1002)] for y in range(1002) ]
penalty = 0.005
for pixel in range(0,x.size+1):
    if pixel%yy != 0:
        print(pixel, pixel-1)
        bpgraph[pixel][pixel-1] = penalty
    if pixel%yy != yy-1:
        print(pixel, pixel+1)
        bpgraph[pixel][pixel+1] = penalty
    if pixel>=yy:
        print(pixel, pixel-yy)
        bpgraph[pixel][pixel-yy] = penalty
    if pixel+yy<=1000:
        print(pixel, pixel+yy)
        bpgraph[pixel][pixel+yy] = penalty

for j in range(1,x.size+1):
        bpgraph[0][j] = ai[j-1]
for i in range(1,x.size+1):
        bpgraph[i][x.size+1] = bi[i-1]

source = 0; sink = x.size+1
g = Graph(bpgraph)
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))

for j in range(1,x.size+1):
    if bpgraph[0][j] == 0:
        x[j-1] = 1;
    else:
        x[j-1] = 0;


#-----------------print image-------------------#
matlable = x.reshape(xx,yy,1)
zero = [[[0 for i in range(2)]for i in range(yy)] for i in range(xx)]
matlable1 = np.concatenate((matlable,zero), axis=2)

for i in range(len(matlable)):
    for j in range(int(matlable.size/len(matlable))):
        #print("!",matlable[i][j])
        if (matlable[i][j][0] == 1):
            #flag = matlable[i][j].pop(0)
            #matlable[i][j] = [0 for i in range(3)]
            matlable1[i][j][0] = image1RGB[i][j][0]
            matlable1[i][j][1] = image1RGB[i][j][1]
            matlable1[i][j][2] = image1RGB[i][j][2]
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

matlable3 = np.concatenate((matlable,zero), axis=2)

for i in range(len(matlable)):
    for j in range(int(matlable.size/len(matlable))):
        #print("!",matlable[i][j])
        if (matlable[i][j][0] == 0):
            #flag = matlable[i][j].pop(0)
            #matlable[i][j] = [0 for i in range(3)]
            matlable3[i][j][0] = image1RGB[i][j][0]
            matlable3[i][j][1] = image1RGB[i][j][1]
            matlable3[i][j][2] = image1RGB[i][j][2]
        else:
            #flag = matlable[i][j].pop(0)
            #matlable[i][j] = [0 for i in range(3)]
            matlable3[i][j][0] = 255
            matlable3[i][j][1] = 255
            matlable3[i][j][2] = 255

matlable4 = matlable3.astype(np.uint8)

pyplot.imshow(matlable4, interpolation='nearest')
pyplot.show() 
#-----------------
#final = [[0 for i in range(col)] for i in range(row)]
#for i in range(xx):
#    for j in range(yy):
#        for k in range(c_row*i, c_row*i+c_row):
#            for m in range(c_col*j, c_col*j+c_col):
#                final[k][m] = matlable[i][j]
#pyplot.imshow(final, interpolation='nearest')
#pyplot.show()
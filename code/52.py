#Program to plot an ellipse 
#Code by GVV Sharma
#August 8, 2020
#Revsed July 31, 2024

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/shivrm/Projects/matgeo/codes/CoordGeo')        #path to my scripts


#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-5,5,len)

#Ellipse parameters
V = np.array(([16,0],[0,1]))
u = np.array(([0,0])).reshape(-1,1)
f = -16
O = -LA.inv(V)@u
#F = np.zeros((2,2))
n,c,F,p = conic_param(V,u,f)
print(n,c,F)

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
a = np.sqrt(-f/D_vec[0])
b = np.sqrt(-f/D_vec[1])
xStandardEllipse = ellipse_gen(a,b)

#Major and Minor Axes
MajorStandard = np.array(([a,0]))
MinorStandard = np.array(([0,b]))

#Affine ellipse parameters
# `F = P@Fstd+O#focus
#Affine transform 
xActualEllipse = P@xStandardEllipse
MajorActual = P@MajorStandard
MinorActual = P@MinorStandard
print(a,b)

f = np.array([0, pow(15,0.5)/16]).reshape(-1,1)

#Plotting the standard ellipse
plt.plot(xStandardEllipse[0,:],xStandardEllipse[1,:],label='Standard ellipse')

#Plotting the actual ellipse
plt.plot(xActualEllipse[0,:],xActualEllipse[1,:],label='Actual ellipse')

#Labeling the coordinates
tri_coords = np.vstack((MinorStandard,-MinorStandard,f.T,-f.T)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['$V1$','$V2$',"F1", "F2"]
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.show()

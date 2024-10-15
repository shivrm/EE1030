#Code by GVV Sharma
#June 12, 2022
#Revised November 14, 2023
#released under GNU GPL
#https://www.gnu.org/licenses/gpl-3.0.en.html

#Drawing a pair of tangents to a conic

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/shivrm/Projects/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#Triangle vertices
O = np.array([0, 0]).reshape(-1,1)
r = 5
A = np.array([10, 0]).reshape(-1,1)


#Incircle parameters

h  = A
V = np.eye(2)
u = -O
f = LA.norm(O)**2-r**2

[x1,x2] = contact(V,u,f,h)

c = circ_gen(O, r)

plt.plot(c[0,:], c[1,:], label="Circ")

t1 = line_gen(A, x1)
plt.plot(t1[0,:], t1[1,:], label="Circ")
t2 = line_gen(A, x2)
plt.plot(t2[0,:], t2[1,:], label="Circ")

# Helper function for annotating a point
def annot(p, lbl):
    # Sorry for the bad code :P
    # Basically p.tolist gives a list of the form [[float_x], [float_y]]
    # I map each list to the integer value of the coordinate
    # e.g. `[float_x]` is mapped to `int_x`
    #   ~shivrm
    coords = tuple(map(lambda x: round(x[0], 2), p.tolist()))
    plt.annotate(f"{lbl}\n{coords}",
                 coords,
                  textcoords="offset points",
                  xytext=(20, -10),
                    ha="center")

annot(O, 'O')
annot(x1, 'x1')
annot(x2, 'x2')
annot(A, 'A')

plt.grid()
plt.axis('equal')

plt.show()

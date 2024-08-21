#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Secion Formula


import sys                                          #for path to external scripts
sys.path.insert(0, '/root/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

# Vertices
P = np.array([-1, 3]).reshape(-1,1)
Q = np.array([2, 5]).reshape(-1,1)

k = 2/3
R = (Q + k*P) / (1 + k)

# Generate lines
x_PR = line_gen(P, R)
x_RQ = line_gen(R, Q)

# Plot all lines
plt.plot(x_PR[0,:], x_PR[1,:],label="$PR$")
plt.plot(x_RQ[0,:], x_RQ[1,:],label="$RQ$")


# Helper function for annotating a point
def annot(p, lbl):
    # Sorry for the bad code :P
    # Basically p.tolist gives a list of the form [[float_x], [float_y]]
    # I map each list to the integer value of the coordinate
    # e.g. `[float_x]` is mapped to `int_x`
    #   ~shivrm
    coords = tuple(map(lambda x: x[0], p.tolist()))
    plt.annotate(f"{lbl}\n{coords}",
                 coords,
                  textcoords="offset points",
                  xytext=(20, -10),
                 ha="center")
annot(P, 'P')
annot(Q, 'Q')
annot(R, 'R')

ax = plt.gca()

ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('fig.pdf')
#else
#plt.show()


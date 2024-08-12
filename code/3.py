#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Secion Formula


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/shivrm/Projects/matgeo/codes/CoordGeo')        #path to my scripts
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
A = np.array([3, -2]).reshape(-1,1)
B = np.array([3, 4]).reshape(-1,1)

M = B - A

if not M[0, 0]:
    m = float("inf")
else:
    m = M[1,0] / M[0, 0]

print("M =", M)
print("m =", m)

# Generate lines
x_AB = line_gen(A, B)

# Plot all lines
plt.plot(x_AB[0,:], x_AB[1,:],label="$AB$")

# Helper function for annotating a point
def annot(p, lbl):
    # Sorry for the bad code :P
    # Basically p.tolist gives a list of the form [[float_x], [float_y]]
    # I map each list to the integer value of the coordinate
    # e.g. `[float_x]` is mapped to `int_x`
    #   ~shivrm
    coords = tuple(map(lambda x: int(x[0]), p.tolist()))
    plt.annotate(f"{lbl}\n{coords}",
                 coords,
                  textcoords="offset points",
                  xytext=(20, -10),
                 ha="center")
annot(A, 'A')
annot(B, 'B')

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
#plt.savefig('chapters/10/7/2/1/figs/fig.pdf')
#subprocess.run(shlex.split("termux-open chapters/10/7/2/1/figs/fig.pdf"))
#else
plt.show()


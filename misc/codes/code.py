import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys
sys.path.insert(0, 'CoordGeo')

#local imports
from CoordGeo.line.funcs import *
from CoordGeo.triangle.funcs import *
from CoordGeo.conics.funcs import *

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 100
y = np.linspace(-5,5,len)

#Patabola parameters
V1 = np.array(([1,0],[0,0]))
u1 = np.array(([1/2,-1/2])).reshape(-1,1)
f1 = 12
n,c,F,O,lam,P,e = conic_param(V1,u1,f1)
flen = parab_param(lam,P,u1)
x = parab_gen(y,flen)
parStandard =np.block([[x],[y]])
Of = O.flatten()
parActual = P@parStandard + Of[:,np.newaxis]

# Circle parameters
V2 = np.array(([1,0],[0,1]))
u2 = np.array(([0, 0])).reshape(-1,1)
f2 = -4
n,c,F,O,lam,P,e = conic_param(V2,u2,f2)
ab = ellipse_param(V2,u2,f2)
circStandard = ellipse_gen(ab[0], ab[1])
Of = O.flatten()
circActual = P@circStandard + Of[:,np.newaxis]

plt.plot(parActual[0,:],parActual[1,:],label='$x^2 + x + 12 = y$')
plt.plot(circActual[0,:],circActual[1,:],label='$x^2 + y^2 = 4$')

qx = np.roots((2,3,26,12))[2]
qy = qx**2 + qx + 12

q1 = np.array([qx, qy]).reshape(-1, 1)
q2 = 2 * q1 / np.linalg.norm(q1)

print('Shortest Distance:', np.linalg.norm(q2 - q1))

line = line_gen(q1, q2)
plt.plot(line[0,:], line[1,:], label="Normal")

plt.legend()
plt.axis('equal')
plt.grid()
plt.savefig('../figs/fig.pdf')
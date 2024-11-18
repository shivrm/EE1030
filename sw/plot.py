import numpy as np
import matplotlib.pyplot as plt

gs_data = np.loadtxt('data/gram_schmidt.dat')
hh_data = np.loadtxt('data/householder.dat')

gs_avg = np.average(gs_data[:, 1:], axis=1)
hh_avg = np.average(hh_data[:, 1:], axis=1)

plt.plot(gs_data[:, 0], gs_avg, label="Gram-Schmidt Method")
plt.plot(hh_data[:, 0], hh_avg, label="Householder Transformations")
plt.xlabel("Size of matrix (n)")
plt.ylabel("Time taken (s)")
plt.legend(loc='best')
plt.grid()

plt.savefig('figs/compare.pdf')
plt.clf()

data = np.loadtxt('data/householder250.dat')

plt.plot(data[:,0], data[:, 1])
plt.xlabel("Size of matrix (n)")
plt.ylabel("Time taken (s)")
plt.grid()

plt.savefig('figs/householder250.pdf')

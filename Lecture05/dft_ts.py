# Adapted this from Newman's dft script
import numpy as np
import pylab as plt


def dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c


y = plt.loadtxt("pitch.txt", float)
plt.subplot(2, 1, 1)
plt.plot(y)
plt.title('pitch timeseries')
c = dft(y)
plt.subplot(2, 1, 2)
plt.plot(abs(c))
plt.title('amplitude of Fourier coefficients')
plt.xlim(0, 500)
plt.show()

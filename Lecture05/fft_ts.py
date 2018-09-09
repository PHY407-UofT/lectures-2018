#various exercises with dft and pft
import numpy as np
import pylab as plt
from numpy.fft import rfft, irfft
from time import time

pi = np.pi
#function to calculate the dft
def dft(y):
    N = len(y)
    c = np.zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*np.exp(-2j*pi*k*n/N)
    return c

#plot time series and dft
y = plt.loadtxt("pitch.txt",float)
plt.subplot(3,1,1)
plt.plot(y)
plt.title('pitch timeseries')
dft_time = time()
c = dft(y)
dft_time = time() - dft_time
plt.subplot(3,1,2)
plt.plot(abs(c))
plt.title('amplitude of fourier coefficients')
plt.xlim(0,500)

#------------------
#now do it again with FFT
fft_time = time()
c2 = rfft(y)
fft_time = time() - fft_time

#compare home made dft with fft performance
print ('dft time {0:10.2e} and fft time {1:10.2e}'.format(dft_time, fft_time))

#plot
plt.subplot(3,1,3)
plt.plot(abs(c2))
plt.title('amplitude of fourier coefficients using fft')
plt.xlim(0,500)

print( 'maximum  |c2-c|: ', max(abs(c2-c)))

#now do things with proper time dimensions and filter out desired frequencies
#sampling frequency for audio signal
f = 44100.0 #Hz
#related temporal sample
dt = 1/f #s
#length of vector
N = len(y)
#length of interval
T = N*dt
#convert to (angular) frequency
freq = np.arange(N/2+1)*2*pi/T
#dimensional time axis
t = np.arange(N)*dt
#sort on maximum frequency
MaxFreqs = np.argsort(abs(c2)**2) #get indexes of largest three frequencies
MaxFreqs = MaxFreqs[-1:-4:-1] #retain only top three
print ('top three frequencies and their amplitudes:')
print ('{0:10.2f} {1:10.2f} {2:10.2f} Hz'.format(freq[MaxFreqs[0]]/(2*pi),freq[MaxFreqs[1]]/(2*pi),freq[MaxFreqs[2]]/(2*pi)))
print ('{0:10.2f} {1:10.2f} {2:10.2f}'.format(abs(c2[MaxFreqs[0]]),abs(c2[MaxFreqs[1]]), abs(c2[MaxFreqs[2]])))

#create a filtered array
c2_filt = np.copy(c2[:])
#zero out desired indices
c2_filt[MaxFreqs] = 0.0
#transform back to time domain
y_filt = irfft(c2_filt)
#now plot things dimensionally
plt.figure(2,figsize=(6,10))
plt.subplot(2,1,1)
plt.plot(t,y, t, y_filt)
plt.xlabel('t(s)')
plt.title('pitch timeseries')
plt.subplot(2,1,2)
plt.plot(freq/(2*pi),abs(c2), freq/(2*pi), abs(c2_filt))
plt.title('amplitude of fourier coefficients')
plt.xlim((0,3000))
plt.xlabel('f (Hz)')
plt.show()
plt.savefig('filtering_lab5.pdf')
plt.figure(3)
#let's plot the cleaned up time series too - just for fun
plt.plot(t,y-y_filt)
plt.xlabel('t(s)')
plt.title('pitch timeseries after removing lower amplitude signals')

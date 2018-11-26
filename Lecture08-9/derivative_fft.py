#calculate derivative of a function using fourier transform method
#import required routines
from numpy import arange, exp, pi
from pylab import plot, legend, show,subplot,xlabel,ylabel
from numpy.fft import rfft, irfft
#define function and its derivative
def f(x):
    return exp(-(x-L/2)**2/Delta**2)
def dfdx(x):
    return exp(-(x-L/2)**2/Delta**2)*-2*(x-L/2)/Delta**2

#define problem parameters
L=2.0
Delta=0.1
nx=200

#define x, f(x), f'(x)
x=arange(0,L,L/nx)

f = f(x)

f_derivative = dfdx(x)

#now do the same thing spectrally:
#fourier transform
fhat = rfft(f)
#define k
karray = arange(nx/2+1)*2*pi/L
#define ik*fhat
fhat_derivative = complex(0,1)*karray*fhat
#and transform back
f_derivative_fft = irfft(fhat_derivative)

subplot(2,1,1)
plot(x,f,x,f_derivative,x,f_derivative_fft)
legend(('f','f derivative', 'f derivative fft'))
xlabel('x')
subplot(2,1,2)
plot(x,abs(f_derivative-f_derivative_fft))
xlabel('x')
ylabel('abs(difference)')

show()
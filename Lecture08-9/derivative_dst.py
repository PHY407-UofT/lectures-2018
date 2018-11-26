from pylab import plot, show, legend, subplot, xlabel, ylabel
from numpy import zeros, empty, linspace, exp, arange,minimum, pi, sin,cos, array
from dcst import dst, idst, dct, idct

N = 256
# x = pi*n/N
x = arange(N)*pi/N
#function is a sine series
f = sin(x)-2*sin(4*x)+3*sin(5*x)-4*sin(6*x)
#do fourier sine series
fCoeffs = dst(f)
print('Original series: f = sin(x)-2sin(4x)+3sin(5x)-4sin(6x)')
for j in range(7):
    print( 'Coefficient of sin(%ix):'%j, fCoeffs[j]/N)

print('See Figure for calculating second derivative')
#second derivative is also a sine series
d2f_dx2_a = -sin(x)+32*sin(4*x)-75*sin(5*x)+144*sin(6*x)
#second derivative using fourier transform
DerivativeCoeffs = -arange(N)**2*fCoeffs
d2f_dx2_b = idst(DerivativeCoeffs)
subplot(2,1,1) 
plot(x,d2f_dx2_a, x, d2f_dx2_b,'+')
xlabel('x')
legend(('analytic','using DST'))
subplot(2,1,2)
plot(x,abs(d2f_dx2_a-d2f_dx2_b))
xlabel('x')
ylabel('abs(diff)')
show()

################################################################
# This program uses the Mean Value Monte Carlo method to evaluate
# the integral of the function f
################################################################
from math import sin,sqrt
from random import random

#define integrand
def f(x):
    return (sin(1/(x*(2-x))))**2

#define constants
N = 10000 #number of points
b=2.0     #end limit of integration
a=0.0     #starting limit of integration


#sums needed for mean value method
ysum = 0.0      #N<f>
ysquaresum=0.0  #N<f**2>

#loop to evaluate integral
for i in range(N):
    
    x = (b-a)*random()  #calculate random point in integration interval
    y = f(x)            #evalue y = f(x)    
    ysum += y           #calculate N<f>
    ysquaresum += y**2  #calculate N<f**2>

#calculate integral
I = 2.0*ysum/float(N)
print"Integral: ",I


#calculate the variance
yvar=ysquaresum/float(N)-(ysum/float(N))**2

#error estimate is (b-a)*sqrt(var f)/sqrt(N)
error=(b-a)*sqrt(yvar)/sqrt(float(N))

print 'error=', error

#error estimate is: 0.00530917688359 which is somewhat smaller than part (a)

#####################################################################
# This program uses a hit or miss Monte Carlo method to integrate f(x)
#####################################################################

from math import sin,sqrt
from random import random

#define integrand
def f(x):
    return (sin(1/(x*(2-x))))**2

#define constants
N = 10000 #number of random samples
count = 0 #intialize counter
b=2.0 #end limit of integration
a=0.0 #starting limit of integration

for i in range(N):
    x = (b-a)*random()   #randomly choose x value in range
    y = random()     #randomly choose y value in range
    if y<f(x):       #check if y is below curve and hence adds to integral
        count += 1

#Calculate integral
I = (b-a)*float(count)/float(N) 
print ('Integral: ',I)
# Integral estimate is: 1.4492

#error estimate is sqrt(I(A-I))/sqrt(N)
A=(b-a) #area of total region from which we are sampling points
error=sqrt(I*(A-I))/sqrt(float(N))
print( 'error=', error)

#error estimate is:   0.00893431228467

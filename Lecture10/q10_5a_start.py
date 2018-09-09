#####################################################################
# This program uses a hit or miss Monte Carlo method to integrate f(x)
#####################################################################

from math import sin,sqrt
from random import random

######################################################################
# User defined function
######################################################################

#define integrand
def f(x):
    return (sin(1./(x*(2.-x))))**2


######################################################################
# Main program starts here
######################################################################

#define constants
N = 1000 #number of random samples
integ = 0.0 #intialize counter
b=2.0 #end limit of integration
a=0.0 #starting limit of integration

#loop over N random x,y points
#check if y is below curve and hence adds to integral
# if so, add to count

for i in range(N):
    #randomly choose x
    x = 2.0 * random()
    
    #check if y < f(x)
    integ += 1

   
#Calculate integral
I = (b-a)*float(integ)/float(N) 
print I
##print 'Integral: ',I
### Integral estimate is: 1.4492

##error estimate is sqrt(I(A-I))/sqrt(N)
#A=(b-a) #area of total region from which we are sampling points
#error=sqrt(I*(A-I))/sqrt(float(N))
#print 'error=', error

#error estimate is:   0.00893431228467

#The following integrates a given function using gaussian quadrature
#import gaussian weight/point calculator
from gaussxw import gaussxw
#import math functions
from math import sin

#define required function
def f(x):
	return x**4 + sin(x**2)


N = 10
a = -1.0
b = 1.0

#calculate weights
x,w = gaussxw(N)

#do summation
s=0.0

for k in range(N):
	s += w[k]*f(x[k])
	
	
print ('Integral of x**4+sin(x**2) from -1 to 1 is ',s)

#This program uses Gaussian Quadrature to integrate a function f(x)

from gaussxw import gaussxw

from math import sin

#define function to integrate
def f(x):
    return x**3+sin(x**2)


#Set number of sample points
N = 20

#set integration limits
a = -1.0
b = 1.0

#Calculate gaussian sample points and weights using external functions
x,w = gaussxw(N)

#calculate integral using Gaussian quadrature
s = 0.0
for k in range(N):
    s += w[k]*f(x[k])

print s
    

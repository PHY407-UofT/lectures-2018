################################################################
#These are a set of functions for different integration methods:
# (1) Trapezoidal rule
# (2) Simpson's rule
# (3) Gaussian quadrature
# Also included are gaussxw and gaussxwab needed for Gaussian quadrature
################################################################

from pylab import *


#Trapezoidal rule
def integrate_trap(xmin,xmax,nx,integrand):
    deltax=(xmax-xmin)/float(nx-1)
    result=0.5*(integrand[0]+integrand[nx-1])
    
    for k in range(1,nx-1):
        result += integrand[k]

    result = result*deltax    
    return(result)

#Simpson's rule
def integrate_simp(xmin,xmax,nx,integrand):
    deltax=(xmax-xmin)/float(nx-1)
    result=integrand[0]+integrand[nx-1]

    for k in range(1,nx,2):        
        result += 4.0*integrand[k]
        
    for k in range(2,nx-1,2):
        result += 2.0*integrand[k]
    result = result*deltax/3.0
    return(result)

#Gaussian Quadrature
def integrate_gaus(nxg,w,integrand):
    #gaussxw has to be called in main program before to get gaussian points and weights
    result=0.0
    for k in range(nxg):
        result +=w[k]*integrand[k]
    return(result)

#function to calculate gaussian weights

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

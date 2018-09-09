#do euler.py solution for odeint
from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show, legend
from scipy.integrate import odeint

def f(x,t):
    return -x**3 + sin(t)

a = 0.0           # Start of the interval
b = 10.0          # End of the interval
N = 1000          # Number of steps
h = (b-a)/N       # Size of a single step
x = 0.0           # Initial condition

tpoints = arange(a,b,h)
xpoints = []
for t in tpoints:
    xpoints.append(x)
    x += h*f(x,t)

#also solve by odeint
x_new = odeint(func=f,y0=0,t=tpoints)

plot(tpoints,xpoints)
xlabel("t")
ylabel("x(t)")
plot(tpoints,x_new+0.2)
legend(('Euler','odeint+0.2'))
show()

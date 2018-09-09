#calculate integral x^4+sin(x^2) from -1 to 1
#import required functions
from math import sin
from gaussxw import gaussxw

#define function (integrand)
def f(x):
    return x**4+sin(x**2)

#generate sample points and weights
N=100
x,w = gaussxw(N)
#calculate integral using formula on board ...
s = 0
for k in range(N):
    s += w[k]*f(x[k])

print('The required integral is ', s)

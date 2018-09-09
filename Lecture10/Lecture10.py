#demonstration of how to generate non-uniform distribution
#import required functions
import pylab as plt
import numpy as np
from numpy.random import seed, random

s = seed(4219)
print ('seed1: random',random(3))
s=seed(4220)
print ('seed2: random',random(3))
s = seed(4219)
print( 'seed1: random',random(3))

N=10000
mu = 1.0
#z is a uniform variate
z = random(N)
#x should be an expontentially distributed variate
x=-(1/mu)*np.log(1-z)

plt.subplot(2,1,1)

plt.hist(z, bins = 100)
plt.title('Uniform distribution')

plt.subplot(2,1,2)

plt.hist(x, bins = 100)
plt.title('Exponential distribution')

plt.show()

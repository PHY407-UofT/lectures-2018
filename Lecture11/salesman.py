from math import sqrt,exp
from numpy import empty
from random import random,randrange
import pylab as plt

N = 25
R = 0.02
Tmax = 10.0
Tmin = 1e-3
tau = 1e4

# Function to calculate the magnitude of a vector
def mag(x):
    return sqrt(x[0]**2+x[1]**2)

# Function to calculate the total length of the tour
def distance():
    s = 0.0
    for i in range(N):
        s += mag(r[i+1]-r[i])
    return s

# Choose N city locations and calculate the initial distance
r = empty([N+1,2],float)
for i in range(N):
    r[i,0] = random()
    r[i,1] = random()
r[N] = r[0]
D = distance()

# Set up the graphics
plt.ion()
plt.show()
plt.figure(1)
h = plt.plot(r[:,0],r[:,1],'k-o')
plt.xlim([0,1])
plt.ylim([0,1])
plt.pause(0.01)

# Main loop
t = 0
T = Tmax
while T>Tmin:
    print('t', t)
    # Cooling
    t += 1
    T = Tmax*exp(-t/tau)

    # Update the visualization every 100 moves
    if t%1000==0:
#    if t%1 == 0:
        h[0].set_xdata = r[:,0]
        h[0].set_ydata = r[:,1]
        plt.clf()
        h = plt.plot(r[:,0],r[:,1],'k-o')
        plt.xlim([0,1])
        plt.ylim([0,1])
        plt.pause(0.01)
    # Choose two cities to swap and make sure they are distinct
    i,j = randrange(1,N),randrange(1,N)
    while i==j:
        i,j = randrange(1,N),randrange(1,N)

    # Swap them and calculate the change in distance
    oldD = D
    r[i,0],r[j,0] = r[j,0],r[i,0]
    r[i,1],r[j,1] = r[j,1],r[i,1]
    D = distance()
    deltaD = D - oldD

    # If the move is rejected, swap them back again
    if random()>exp(-deltaD/T):
        r[i,0],r[j,0] = r[j,0],r[i,0]
        r[i,1],r[j,1] = r[j,1],r[i,1]
        D = oldD

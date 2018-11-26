#################################################################
# This programs calculates the total energy for N dipoles in a
# 1D lattice
#################################################################

from numpy import zeros,sum, copy
from pylab import plot, show, legend, pause, ion,ylim, clf, subplot, draw, ion
from math import exp
from random import random, randrange

########################################################
# user-defined functions
########################################################

# Define function to calculate total energy for the spin state.
def energy(state):
    J=1.0
    return -J*sum(state[0:N-1]*state[1:N])

# Define function to calculate total magnetization for the spin state.        
def magnetization(state):
    return sum(state)


########################################################
# main program starts here
########################################################
ion()
# define constants N (number of spins), J (exchange energy)
N=10
simlen=350000
kb=1.0
T, snapshot = 0.001,1
#T, snapshot = 0.001, 3000
beta=1.0/(kb*T)

#initialize spin state array
state = zeros(N,int)

#initialize lists to store E and M
Elist = []
Mlist = []

#set initial spins randomly
for i in range(N):
    if random() < 0.5:
        state[i] = 1
    else:
        state[i] = -1
#print state

#calculate energy of initial state
E = energy(state)
#print E
Elist.append(E)

#calculate magnetization of initial state
M = magnetization(state)
#print M

Mlist.append(M)


#create loop to update states
for i in range(simlen):
    #create new state by randomly flipping 1 spin state
    test=copy(state)
    picked = randrange(0,N)

    test[picked] = -test[picked]
    #calculate new energy
    E_test = energy(test)
    deltaE = E_test-E
    #calculate acceptance probability
    #accept or reject new state?
    if deltaE <= 0.0:
        state=test
        E = E_test
        M = magnetization(test)
    else:
        p = exp(-beta*deltaE)
        if random() <= p:
            state=test
            E = E_test
            M = magnetization(test)
        
            

    #store energy & magnetization info
    Elist.append(E)
    Mlist.append(M)
    if i%snapshot==0:
        clf()
        subplot(2,1,1)
        for j in range(N):
            plot([j*2,j*2],[-1,1],'k')
            if state[j]>0:
                plot([j*2],[1],'ro',markersize=6)
                plot([j*2],[-1],'bo',markersize=6)  
            else:
                plot([j*2],[1],'bo',markersize=6)
                plot([j*2],[-1],'ro',markersize=6)  
        ylim((-2,2))
        subplot(2,1,2)
        plot(Mlist, 'k')
        pause(0.001)
        
plot(Elist,'b')
plot(Mlist,'r')
legend(('E','M'))
show()

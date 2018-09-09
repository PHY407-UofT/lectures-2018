#################################################################
# This program calculates the total energy and magnetization
# for a 1D Ising model with N dipoles 
#################################################################

#import modules
from __future__ import division
from numpy import ones, sum
from random import random, randrange

########################################################
# user-defined functions
########################################################

#define function to calculate energy
def energyfunction(dipoles):
    energy=-sum(dipoles[0:-2]*dipoles[1:-1])
    return energy


#define function for magnetization

########################################################
# main program starts here
########################################################

#define constants

kb=1.0
T = 1.0
J = 1.0
num_dipoles = 100
N = 100

#generate array of dipoles

dipoles = ones(num_dipoles,int)
energy=[]
magnet=[]

E=energyfunction(dipoles)
energy.append(E)
#calculate magnetization M
magnet.append(M)
print dipoles

for i in range(N):
    picked = randint(0,num_dipoles)
    dipoles[picked]*=-1
    Enew = energyfunction(dipoles)

    #define a few lines of code to decide whether to accept this state.
    
        #if yes, accept this change
        #if not, revert to old state
    #calculate acceptance probability

#store energy and magnetization


#plot energy, magnetization
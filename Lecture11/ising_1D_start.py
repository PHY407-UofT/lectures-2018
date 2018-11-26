# This program calculates the total energy and magnetization
# for a 1D Ising model with N dipoles
# Author: Nico Grisouard, University of Toronto
# Date: 20 November 2018

# import modules
import numpy as np
from random import random, randrange


def energyfunction(dipoles):
    """ function to calculate energy """
    energy = -np.sum(dipoles[0:-1]*dipoles[1:])
    return energy

# define function for acceptance probability


# define function for magnetization


# define constants
kB = 1.0
T = 1.0
J = 1.0
num_dipoles = 100
N = 100

# generate array of dipoles
dipoles = np.ones(num_dipoles, int)
energy = []
magnet = []

E = energyfunction(dipoles)
energy.append(E)
magnet.append()
print(dipoles)

for i in range(N):
    picked = randrange(0, num_dipoles)
    dipoles[picked] *= -1
    Enew = energyfunction(dipoles)

    # calculate acceptance probability
    accepted = acceptance(Enew, E,)

# store energy and magnetization


# plot energy, magnetization

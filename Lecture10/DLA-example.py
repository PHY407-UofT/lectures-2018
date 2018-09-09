#################################################################
# This program simulates diffusion limited aggregation on an LxL grid.
# Particles are initiated until the centre point is filled.
#################################################################
from random import randint
import pylab as plt
import numpy as np
def nextmove(x,y):
    direction=randint(1,4)

    # randomly choose a direction
    # 1 = up, 2 = down, 3 = left, 4=right

    if direction==1:
        #move up
        y+=1
    elif direction==2:
        #move down
        y-=1
    elif direction==3:
        #move right
        x+=1 
    elif direction==4:
        #move left
        x-=1
    else:
        print("error: direction isn't 1-4")
        
    return x,y

#############################################################
# main program starts here
#############################################################



Lp=101 # size of domain
N=100 # number of particles
anchored=np.zeros((Lp,Lp),dtype=int) # array to represent whether each gridpoint has an anchored particle
anchored_points=[[],[]] # list to represent x and y positions of anchored points
centre_point=(Lp-1)/2 # middle point of domain

# set up animation of anchored points
animation_interval=50 # how many moves to make before updating plot of Brownian motion
plt.ion()
plt.figure(1)
plt.title('Diffusion-limited aggregation run for 100 particles')
moving_plot=plt.plot(centre_point,centre_point,'.r',markersize=10)
anchored_plot=plt.plot(anchored_points[0],anchored_points[1],'.k',markersize=10)
plt.xlim([-1,Lp])
plt.ylim([-1,Lp])
plt.xlabel('x')
plt.ylabel('y')

for j in range(N):
    xp = centre_point
    yp = centre_point
    i=0 # counter to keep track of animation of moving particle
    
    not_stuck=True
    while not_stuck:
        if xp==0 or xp==Lp-1 or yp==0 or yp==Lp-1: # Check if the particle has reached a wall
            anchored[xp,yp]=1
            anchored_points[0].append(xp)
            anchored_points[1].append(yp)
            anchored_plot[0].set_xdata(anchored_points[0])
            anchored_plot[0].set_ydata(anchored_points[1])
            plt.draw()
            not_stuck=False
        elif anchored[xp-1:xp+2,yp-1:yp+2].any(): # Check if particle is adjacent to an anchored particle
            anchored[xp,yp]=1
            anchored_points[0].append(xp)
            anchored_points[1].append(yp)
            anchored_plot[0].set_xdata(anchored_points[0])
            anchored_plot[0].set_ydata(anchored_points[1])
            plt.draw()
            plt.pause(0.01)
            not_stuck=False
        else: # If neither of the above, move particle and continue while loop
            i+=1
            xp,yp=nextmove(xp,yp)
            if i%animation_interval==0:
                moving_plot[0].set_xdata(xp)
                moving_plot[0].set_ydata(yp)
                plt.draw()
                plt.pause(0.01)

plt.ioff()

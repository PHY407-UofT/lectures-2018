#relaxation demo
#import functions and plotting routines

from numpy import arange,tanh,cosh
from pylab import plot, show, pause,legend, title,grid
def func(x):
    #return tanh(a*x)-x
    return a*x**2-x
def funcp(x):
    return 2*a*x-1
    #return a/(cosh(a*x))**2-1
#set a
a=3.5
#set initial x
x = 0.8
xplot = arange(0,x,0.01)
xold = x
xnew = x
plot(xplot,func(xplot),'k')
title('newton method demo')

grid()
pause(0.01)
inp=input('press return to continue:')
while True:
    #horizizontal line
    xold = xnew
    xnew = xold-func(xold)/funcp(xold)
    plot([xold,xnew],[func(xold),0],'r-')
    inp=input('press return to continue and x to stop:')
    print( 'current root is ', xnew)
    plot([xnew,xnew],[0,func(xnew)],'r-')
    
    pause(0.01)
    if (inp=='x'):
        break
print ('rooty is ', xnew)
#run loop during which you update the plot and the draw the lines

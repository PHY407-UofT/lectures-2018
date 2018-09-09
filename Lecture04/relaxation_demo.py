#relaxation demo
#import functions and plotting routines

from numpy import arange,tanh
from pylab import plot, show, pause,legend, title
#set a
a=0.5
a=1.8
#set initial x
x = 0.3
xplot = arange(0,1,0.01)
xold = x
xnew = x
plot(xplot,xplot, 'k',xplot,tanh(a*xplot),'g')
legend(('y=x','y=tanh(%sx)'%str(a)),loc='upper left')
title('relaxation method demo')
pause(0.01)
while True:
    #vertical then horizizontal line
    
    plot([xnew,xnew],[xnew,tanh(a*xnew)],'r-')
    plot([xold,xnew],[tanh(a*xold),tanh(a*xold)],'r-')
    xold = xnew
    xnew = tanh(a*xold)    
    x=input('press return to continue and x to stop:')
    
    pause(0.01)
    if (x=='x'):
        break
print( 'root is ', xnew)
#run loop during which you update the plot and the draw the lines

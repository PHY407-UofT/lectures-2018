#example to illustrate machine error using large error constant C to make it easier to see graphically
#import normal distribution
from numpy.random import normal
from numpy import arange
#import plotting functions
from pylab import hist, show, subplot, figure, xlabel,xticks, legend, savefig
#import rcparams to change font size
from matplotlib import rcParams
rcParams.update({'font.size':14, 'legend.fontsize':10})
#define array size
N = 1000000
#define numbher of bins for histogram
N_Bins = 100
#define C, which is our simulated error constant
C=1e-2

#define a few numbers x
#x1,x2 = (-0.2,0.25)

#define numbers
(x1,x2) = (3,-3.2)
#define errors in terms of C
sigma1 = C*abs(x1)
sigma2 = C*abs(x2)
#define distributions to those numbers satisfying sigma = Cx
#This is how we simulate error.
d1  = normal(loc=x1, scale=sigma1, size=N)
d2  = normal(loc=x2, scale=sigma2, size=N)

#then add up the distributions
#then calculate the distribution of the sums.
sumd = d1 + d2

figure(1, figsize=((7,12)))
#plot histograms of the two numbers and their sum
ax = subplot(2,1,1)
hist(d1,N_Bins, histtype='stepfilled')
hist(sumd, N_Bins,  histtype='stepfilled')
hist(d2, N_Bins, histtype='stepfilled')
leg=legend((str(x1),'sum',str(x2)),loc='upper left')
ax.grid(True)
xlabel('mean + absolute error')

#then plot fractional error by diving by the mean values.
#fractional errors will be large for opposite-signed large numbers
#offset and spread have to be adjusted to make the plots clear.
ax = subplot(2,1,2)
offset = 2
spread = offset/4.0
hist(-offset+(d1-x1)/x1,N_Bins,histtype='stepfilled')

hist((sumd-(x1+x2))/(x1+x2),N_Bins,histtype='stepfilled')
hist(offset+(d2-x2)/x2,N_Bins,histtype='stepfilled')

xticks([-offset-spread,-offset,-offset+spread,-spread,0,spread,offset-spread,offset,offset+spread],
       [str(-spread),str(0.0),str(spread),str(-spread),str(0.0),str(spread),str(-spread),str(0.0),str(spread)])

ax.grid(True)


xlabel('fractional error')
savefig('MachineError_x1='+str(x1)+'_x2='+str(x2)+'.png')

#this plot just shows the a single number and its error
figure(2, figsize=((7,7)))
hist(d1,N_Bins, histtype='stepfilled')
xlabel('mean +- absolute error:'+str(x1)+' +- '+str(sigma1))
savefig('MachineError_x1='+str(x1)+'.png')
show()

from numpy import array,empty, copy
from numpy.linalg import solve

def GaussElim(A_in,v_in, pivot = False):
    
    A = copy(A_in)
    v = copy(v_in)
    N = len(v)
    
    for m in range(N):
        #do partial pivots if required
        if (pivot):
            swap_index = m
            for k in range(m+1,N):
                if abs(A[k,m])>abs(A[swap_index,m]):
                    #identify swap row
                    swap_index = k
            if swap_index > m:
                #carry out swap on v and A
                v_pivot = v[swap_index]
                v[swap_index] = v[m]
                v[m] = v_pivot
                A[m,:], A[swap_index,:] = copy(A[swap_index,:]), copy(A[m,:])
            
        # Divide by the diagonal element
        div = A[m,m]
        A[m,:] /= div
        v[m] /= div
    
        # Now subtract from the lower rows
        for i in range(m+1,N):
            mult = A[i,m]
            A[i,:] -= mult*A[m,:]
            v[i] -= mult*v[m]
    
    # Backsubstitution
    x = empty(N,dtype = v.dtype)
    for m in range(N-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,N):
            x[m] -= A[m,i]*x[i] 
    return x
    
def PartialPivot(A_in,v_in):
    return GaussElim(A_in, v_in, pivot=True)    



example = input('Enter an example [1-3]: ')
example = int(example)

if example==1:
    A = array([[1,2],[3,4]],float)
    v = array([5,6], float)
if example == 2:

    A = array([[1e-20,1],[1,1]],float)
    v = array([1,0], float)
    x = solve(A,v)
    print ('A is ', A)
    print ('v is ', v)
    print ('x from linalg.solve is',x)
    print ('but x from gaussian elimination is...')

if example == 3:
    A = array([[1e-20,1],[1,1]],float)
    v = array([1,0], float)
    x = PartialPivot(A,v)
    print ('A is ', A)
    print ('v is ', v)
    print ('x from PartialPivot is',x)
    print ('but x from gaussian elimination is...')
    

N = len(v)

# Gaussian elimination

for m in range(N):

    # Divide by the diagonal element
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print(x)

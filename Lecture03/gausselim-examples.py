from numpy import array,empty, copy
from numpy.linalg import solve

example = input('Enter an example [1-2]: ')
example = int(example)

if example==1:
    
    A = array([[1,2],[3,4]],float)
    A_copy = copy(A)
    v = array([5,6], float)
if example == 2:

    A = array([[1e-20,1],[1,1]],float)
    v = array([1,0], float)
    x = solve(A,v)
    print( 'A is ', A)
    print('v is ', v)
    print( 'x from linalg.solve is',x)
    print('but x from gaussian elimination is...')


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

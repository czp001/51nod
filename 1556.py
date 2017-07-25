p=10**9+7
inv=[0]*(10**6+10)
inv[1]=1
for i in range(2,10**6+10):
    inv[i] = p - ((p/i * inv[p%i] % p))
    
M=[0]*(10**6+10)
M[1],M[2]=1,2
for n in xrange(3,10**6+10):
    M[n]=(2*n*M[n-1]+3*(n-2)*M[n-2])*inv[n]%p
    
n=input()
print M[n]

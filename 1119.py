p=10**9+7
N=10**6

inv=[0]*(N+2)
inv[1]=1
for i in range(2,N+2):
    inv[i] = p - ((p/i * inv[p%i] % p))

def C(n,k,p):
    k=min(n-k,k)
    t=1
    for i in xrange(1,k+1):
        t=t*inv[i]*(n+1-i)%p
    return t
a,b=map(int,raw_input().split())
print C(a+b-2,a-1,p)

p=1000000007
N=2000

inv=[0]*(N+2)
inv[1]=1
for i in range(2,N+2):
    inv[i] = p - ((p/i * inv[p%i] % p))
    
C = [[0 for col in range(N+2)] for row in range(N+1)]
C[0][1]=1
for k in range(1,N+1):
    s=1
    for i in range(k+1,1,-1):
        C[k][i]=k*inv[i]*C[k-1][i-1]%p
        s=(s-C[k][i])%p
    C[k][1]=s
    
def S(n,m,p):
    s=0
    t=1
    for i in range(1,m+2):
        t=t*n%p
        s=(s+t*C[m][i])%p
    return s
    
d=input()
for i in range(d):
    n,k=map(int,raw_input().split())
    print S(n,k,p)

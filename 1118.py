p=10**9+7
N=2000
fac=[1]*N
invf=[1]*N
for i in range(2,N):
    fac[i]=i*fac[i-1]%p
invf[N-1]=pow(fac[N-1],p-2,p)
for i in range(N-2,-1,-1):
    invf[i]=invf[i+1]*(i+1)%p
def C(n,m):
    return fac[n]*invf[m]*invf[n-m]%p
a,b=map(int,raw_input().split())
print C(a+b-2,a-1)

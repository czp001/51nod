from math import pi
p=10**9+7
N=10**6+1

fac=[1]*N
inv=[1]*N
for i in range(2,N):
    fac[i]=i*fac[i-1]%p
    inv[i] =(p-p//i) * inv[p%i] % p

for i in range(2,N):
    inv[i]=inv[i]*inv[i-1]%p
    
def bino(n,m):
    return fac[n]*inv[m]*inv[n-m]%p

n=int(input())
if(n<4):
    print(1)
else:
    ans=0
    for i in range(n-4+1):
        j=int((n-4-i)/pi)
        ans+=bino(i+j,i)
    for i in range(int((n-4)/pi)+1):
        j=int(n-4-pi*i)
        ans+=bino(i+j,i)
    print(ans%p)

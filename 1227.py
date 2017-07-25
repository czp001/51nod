N=10**6
prime=[0]*N
vst=[0]*N
phi=[0]*N
phi[1]=1
num=0
p=10**9+7

def s1(l,r):
    return (l+r)*(r-l+1)//2%p

for i in range(2,N):
    if(not vst[i]):
        prime[num]=i
        phi[i]=i-1
        num+=1
    j=0
    while(prime[j]*i<N and j<num):
        vst[prime[j]*i]=1
        if(i%prime[j]):
            phi[i*prime[j]]=phi[i]*(prime[j]-1)
        else:
            phi[i*prime[j]]=phi[i]*prime[j]
            break
        j=j+1
for i in range(2,N):
    phi[i]=(phi[i-1]+i*phi[i])%p
    
cache={}
def S(n):
    if n<N:return phi[n]
    if n in cache:return cache[n]
    ans,i=n*(n+1)*(2*n+1)*(p+1)//6%p,2
    while i<=n:
        k=n//i
        j=n//k
        ans=(ans-S(k)*s1(i,j))%p
        i=j+1
    cache[n]=ans
    return ans

def F(n):
    ans,i=n,1
    while i<=n:
        k=n//i
        j=n//k
        ans=(ans+S(k)*(j-i+1))%p
        i=j+1
    return ans*(p+1)//2%p

a,b=map(int,raw_input().split())
print (F(b)-F(a-1))%p

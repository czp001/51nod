from math import sqrt

N=15*10**6
p=10**9+7
prime=[0]*N
phi=[0]*N
vst=[0]*N
phi[0],phi[1]=1,1

num=0
for i in range(2,N):
    if(not vst[i]):
        prime[num]=i
        phi[i]=i-1
        num+=1
    j=0
    while(prime[j]*i<N and j<num):
        vst[prime[j]*i]=1
        if(i%prime[j]):
            phi[i*prime[j]]=phi[i]*(prime[j]-1)%p
        else:
            phi[i*prime[j]]=phi[i]*prime[j]%p
            break
        j=j+1

sphi=[0]*N  
sphi[1]=1
for i in range(2,N):
    sphi[i]=(sphi[i-1]+phi[i])%p   

cache={}
def S(n):    
    if n<N:
        return sphi[n]
    elif n in cache:
        return cache[n]
    else:
        v=int(sqrt(n))
        s1=0
        for x in range(1,v+1):
            s1=s1+S(x)*(n//x-n//(x+1))
        s2=0
        for k in range(2,n//(v+1)+1):
            s2=s2+S(n//k)
        t=n*(n+1)//2-s1-s2
        t=t%p
        cache[n]=t
    return t
        
n=int(input())
print(S(n))

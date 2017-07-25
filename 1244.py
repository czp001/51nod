from math import sqrt
N=2*10**7

prime=[0]*N
mu=[0]*N
vst=[0]*N
mu[0],mu[1]=1,1
num=0

for i in range(2,N):
    if(not vst[i]):
        prime[num]=i
        mu[i]=-1
        num+=1
    j=0
    while(prime[j]*i<N and j<num):
        vst[prime[j]*i]=1
        if(i%prime[j]):
            mu[i*prime[j]]=-mu[i]
        else:
            mu[i*prime[j]]=0
            break
        j=j+1

for i in range(2,N):
    mu[i]=mu[i-1]+mu[i]


def M(n,cache={}):     
    if n <N:
        return mu[n]
    elif n in cache:
        return cache[n]
    else:
        v=int(sqrt(n))
        s1=0
        for x in range(1,v+1):
            s1=s1+M(x)*(n//x-n//(x+1))
        s2=0
        for k in range(2,n//(v+1)+1):
            s2=s2+M(n//k)
        t=1-s1-s2
        cache[n]=t
    return t

a,b=map(int,raw_input().split())
print(M(b)-M(a-1))

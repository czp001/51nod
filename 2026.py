from math import sqrt
N=1000000
p=10**9+7
prime=[0]*N
mu=[0]*N
vst=[0]*N
mu[1]=1
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

for i in range(1,N):
    mu[i]=(mu[i-1]+i*mu[i])

def ss(n):
	return n*(n+1)//2

def M(n,cache={}):     
    if n <N:
        return mu[n]
    elif n in cache:
        return cache[n]
    else:
        s,i,j=0,2,0
        while j<n:
            j=n//(n//i)
            s=s+M(n//i)*(ss(j)-ss(i-1))
            i=j+1
        t=1-s
        cache[n]=t
    return t

def S(n):
	s,i,j=0,1,0
	while i<n:
		j=n//(n//i)
		s=s+(n//i)*(M(j)-M(i-1))
		i=j+1
	return s*s%p
n=input()
print S(n)

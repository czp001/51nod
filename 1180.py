N=5000000+5

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
ans=0
m,n=map(int,raw_input().split())
m,n=m-1,n-1
if m==0 and n==0:print 0
elif n==0 or m==0:print 1
else:
    for i in range(1,n+1):
        ans+=mu[i]*(m//i)*(n//i)
    print ans+2

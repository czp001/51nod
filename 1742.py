N=40000
prime=[0]*N
vst=[0]*N
mu=[0]*N
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
f={}
def F(n):
    if n in f:return f[n]
    ans=n
    for i in range(1,int(n**0.5)+1):
        ans=ans-n//(i*i)*mu[i]
    f[n]=ans
    return ans

def S(n):
    s,i=0,1
    while i<=n:
        k=n//i
        j=n//k
        s=s+F(k)*(j-i+1)
        i=j+1
    return s

a,b=map(int,raw_input().split())
print(S(b)-S(a-1))

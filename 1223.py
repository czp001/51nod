from math import sqrt

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def S(n,st,nd):
    ans=0
    if nd>n:nd=n
    x=st
    while x<=nd and x*x<=n:
        ans+=n//x
        x+=1
    if x>nd:return ans
    x-=1
    xpre=x
    x=n//x
    while x:
        xnxt=n//x
        if xnxt>nd:xnxt=nd
        ans+=x*(xnxt-xpre)
        xpre=xnxt
        if xnxt==nd:break
        x-=1
    return ans

N=10**6
p=prime_sieve(N)

mu=[1]*(N+1)
for i in p:
    for j in range(1,N//i**2+1):
        mu[j*i**2]=0
for i in p:
    for j in range(1,(N//i)+1):
        mu[i*j]=mu[i*j]*(-i)
for n in range(1,N+1):
    if abs(mu[n])<n:mu[n]=(-1)*mu[n]
    if mu[n]>0:mu[n]=1
    if mu[n]<0:mu[n]=-1

L=int(input())
z=0
for d in range(1,int(L**0.5)+1):
    if not mu[d]:continue
    l=L//d//d
    z2=0
    for y in range(1,int(l**0.5)+1):
        z2+=S(l//y,y+1,2*y-1)
    z+=z2*mu[d]
print(z)

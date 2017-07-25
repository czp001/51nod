from math import sqrt

N=10**6+1
mod=10**9+7

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

p=prime_sieve(int(sqrt(N)))

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
for n in range(2,N):
    mu[n]=n*mu[n]
mu[0]=0
for n in range(1,N):
    mu[n]=mu[n-1]+mu[n]
cache={}
def S(n):
    if n <N:
        return mu[n]
    elif n in cache:
        return cache[n]
    else:
        v=int(sqrt(n))
        s1=0
        for x in range(1,v+1):
            s1=(s1+S(x)*(n//x-n//(x+1))*(n//x+n//(x+1)+1)//2)
        s2=0
        for k in range(2,n//(v+1)+1):
            s2=(s2+k*S(n//k))
        t=(1-s1-s2)        cache[n]=t
    return t

def factor(n):
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n //= p        while n%p == 0:
            e += 1; n //= p
        F.append([p,e])
    F.sort()
    return F


def trial_division(n, bound=None):
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n%p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m*m <= n:
        if n%m == 0:
            return m
        m += dif[i%8]
        i += 1
    return n

ds,gg=0,{}
for i in range(1,32000+1):
    t=1
    pl=factor(i)
    for j in pl:
        t=(t*(j[0]**(j[1]+1)-1)//(j[0]-1))
    ds=(ds+t)
    gg[i]=ds

def g(n):
    if(n<32000):
        return gg[n]
    else:
        s, d, q = 0, 1, n
        while d < q:
            s = (s + q * (q + 1 + 2 * d) // 2)
            d = d + 1
            q = n // d
        t=(s - d * (d - 1) // 2 * d + q * (q + 1) // 2)
        gg[n]=t
        return t

s=0
n=int(input())
for i in range(1,int(sqrt(n))+1):
    j=n//i
    m=(S(i)-S(i-1))*g(n//i)**2
    s=s+m
    if(n//i==n//(i+1)+1):
        s=(s+(S(n//i)-S(n//i-1))*g(i)**2)
    else:
        s=(s+(S(n//i)-S(n//(i+1)))*g(i)**2)
    if(i==j):
        s=s-m

print(s%mod)

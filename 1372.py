from math import log
mod=10**9+7

def primes(N):
    is_prime = [1] * (N + 1)
    is_prime[0] = 0
    v = int(N**0.5)
    for p in range(2, v + 1):
        if not is_prime[p]:
            continue
        for k in range(p * p, N + 1, p):
            is_prime[k] = 0
    return [p for p in range(2, N + 1) if is_prime[p]]

def pp(n,p):
    s=0
    for i in range(1,int(log(n)/log(p))+1):
        s=s+n//p**i
    return s

def factor(n):
    fs=[]
    pl=primes(n)
    for i in pl:
        fs=fs+[[i,pp(n,i)]]
    fs[0][1]=fs[0][1]-1
    return fs
    
def S(n):
    fl=factor(n)
    t=1
    for i in fl:
        p,k=i[0],i[1]
        t=t*((k+1)*p**k-k*p**(k-1))%mod
    return t

n=int(input())
for i in range(n):
    m=int(input())
    if m==2:
        print('Case #'+str(i+1)+': 1')
    elif m==3:
        print('Case #'+str(i+1)+': 5')
    else:
        print('Case #'+str(i+1)+': '+str(S(m)))

from math import log
mod=10**9+7

def primes(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def pp(n,p):
    s=0
    for i in range(1,int(log(n)/log(p))+1):
        s=s+n//p**i
    return s

n=int(input())
pl=primes(n+1)
ans=1
for i in pl:
    ans=ans*(pp(n,i)*2+1)

print((ans+1)//2%mod)

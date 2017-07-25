p=1000000009
N=100005

fac=[1]*N
for i in xrange(1,N):
    fac[i]=fac[i-1]*i%p

A,B=[1]*N,[1]*N
for i in xrange(1,N):
    A[i]=A[i-1]*691504013%p
    B[i]=B[i-1]*308495997%p

def S(n,k):
    s=0
    for r in xrange(k+1):
        t = A[k-r] * B[r] % p
        x = fac[k]
        y = fac[k-r] * fac[r] % p
        c = x * pow(y,p-2,p) % p
        tmp = t * (pow(t,n,p) - 1) % p * pow(t-1,p-2,p) % p
        if(t == 1):
            tmp = n % p
        tmp = tmp * c % p
        if(r&1):
            s=s-tmp
        else:
            s=s+tmp
        s=s%p
    m=pow(383008016,p-2,p)
    s=s*pow(m,k,p)%p
    return s

d=input()
a,b=[],[]
for i in range(d):
    n,k=map(int,raw_input().split())
    a.append(n)
    b.append(k)

for i in range(d):
    print S(a[i],b[i])

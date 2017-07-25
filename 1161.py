n,k=map(int,raw_input().split())
c=[1]*n
p=10**9+7
a=[int(input()) for i in xrange(n)]
for i in xrange(1,n):
    c[i]=c[i-1]*(k-1+i)*pow(i,p-2,p)%p
c.reverse()
for i in xrange(1,n+1):
    s=0
    for j in xrange(i):
        s=s+a[j]*c[-(i-j)]
    print(s%p)

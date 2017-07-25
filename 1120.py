n=input()
p=10007
def binomial(n, k):      
    if(n<k):return 0
    nt = 1
    for t in xrange(min(k, n-k)):
        nt = nt * (n-t) // (t+1)
    return nt

def lucas(n,k,p):
    res=1
    while(n and k):
        res=res*binomial(n%p,k%p)
        n=n//p
        k=k//p
    return res%p
print(2*lucas(2*n-2,n-1,p)*pow(n,p-2,p)%p)

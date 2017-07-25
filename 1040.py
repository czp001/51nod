def phi(n):
    res,i=n,2
    while(i*i<=n):
        if(n%i==0):
            res=res-res/i
            while(n%i==0):
                n=n/i
        i=i+1
                
    if(n>1):
        res=res-res/n
    return res

n=input()
ans,i=0,1
while(i*i<=n):
    if(n%i==0):
        ans=ans+i*phi(n/i)
        if(n!=i*i):
            ans=ans+(n/i)*phi(i)
    i=i+1
print ans

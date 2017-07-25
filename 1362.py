def binomial(n, k):      
    if(n<k):return 0
    nt = 1
    for t in range(min(k, n-k)):
        nt = nt * (n-t) // (t+1)
    return nt

def solve(n,m,x):
    ans=0
    for i in range(n+1):
        ans=ans+binomial(n,i)%x*binomial(n+m-i+1,n+1)%x
    return ans%x
    
n,m,x=map(int,raw_input().split())
print(solve(n,m,x))

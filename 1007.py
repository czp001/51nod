N=10**4+5
a,dp,s=[0]*N,[0]*N,0
n=input()
for i in range(n):
    a[i]=input()
    s+=a[i]
for i in range(n):
    j=s//2
    while j>=a[i]:
        dp[j]=max(dp[j],dp[j-a[i]]+a[i])
        j-=1
print abs(dp[s//2]-(s-dp[s//2]))

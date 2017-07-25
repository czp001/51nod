n,k=map(int,input().split())
dp=[0 for x in range(k+1)]
for i in range(1,n+1):
    a,b=map(int,input().split())
    for j in range(k,0,-1):
        if j-a>=0:
            dp[j]=max(dp[j],dp[j-a]+b)
        else: 
            break
print (dp[k])

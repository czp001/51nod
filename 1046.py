d=input()
a=[]
for i in range(d):
    t=input()
    a.append(t)
a=[0]+a
dp=[0]*(d+1)
ans=-10**10
for i in range(1,d+1):
    dp[i]= max(dp[i-1] + a[i],a[i])
    ans=max(ans,dp[i])

print ans

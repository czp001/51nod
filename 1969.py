ans={0:1}
for k in range(1,26000):
    if k%2:
        ans[k*(3*k+1)/2]=-1
        ans[k*(3*k-1)/2]=-1
    else:
        ans[k*(3*k+1)/2]=1
        ans[k*(3*k-1)/2]=1
mod=10**9+7
t,b=map(int,raw_input().split())
s=0
for i in range(1,t+1):
    n=input()
    if n in ans:
        nn=ans[n]
    else:nn=0
    s=s+(nn%998244353)*pow(b,t-i,mod)
    s=s%mod
print s

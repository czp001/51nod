N=5*10**6+5
p,vis,g,mu,s=[0]*N,[0]*N,[0]*N,[0]*N,[0]*N
cnt=0
mu[1]=1
for i in range(2,N):
    if not vis[i]:
        p[cnt]=i
        mu[i]=-1
        g[i]=1
        cnt+=1
    j=0
    while(p[j]*i<N and j<cnt):
        vis[i*p[j]]=1
        if i%p[j]:
            mu[i*p[j]] = -mu[i]
            g[i*p[j]] = mu[i] - g[i]
        else:
            mu[i*p[j]]=0
            g[i*p[j]]=mu[i]
            break
        j=j+1
for i in range(1,N):
    s[i]=s[i-1]+g[i]
t=input()
for i in range(t):
    m,n=map(int,raw_input().split())
    if n>m:
        n,m=m,n
    ans,i=0,1
    while i<=n:
        end=min(n//(n//i),m//(m//i))
        ans+=(n//i)*(m//i)*(s[end]-s[i-1])
        i=end+1
    print(ans)

m,n=map(int,raw_input().split())
a=[[0]*m for i in range(n)]
ans=-10**12
for i in range(n):
    a[i]=map(int,raw_input().split())
for i in range(n):
    c=[0]*505
    for j in range(i,n):
        for k in range(m):
            c[k]=c[k]+a[j][k]
        s=-10**12
        for i in range(m):
            s=max(c[i],s+c[i])
            ans=max(ans,s)
print ans

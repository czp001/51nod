a,b,c,ans=[0]*31,[0]*31,[0]*31,50
n,x=map(int,raw_input().split())
for i in range(31):
    if (x&(1<<i))==0:b[i]=0
    else:b[i]=1
for i in range(n):
    t=input()
    f=1
    for j in range(31):
        if (t&(1<<j))==0:a[j]=0
        else:a[j]=1
        if not b[j] and a[j]:
            f=0
            break
    if f:
        for j in range(31):
            c[j]+=a[j]
for i in range(31):
    if b[i]:ans=min(ans,c[i])
print ans

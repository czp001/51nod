a=[0]*100010
n=input()
h=map(int,raw_input().split())
a[0]=1
a[n-1]=1
for i in range(1,n):
    a[i]=min(h[i],a[i-1]+1)
for i in range(n-1,-1,-1):
    a[i]=min(a[i],a[i+1]+1)
ans=0
for i in range(n):
    ans=max(ans,a[i])
print ans

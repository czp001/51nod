a=[]
n,m=map(int,raw_input().split())
for i in range(n):
    a.append(input())
a.sort()
l,r=0,n-1
ans=0
while l<=r:
    if l==r:
        ans+=1
        break
    if a[l]+a[r]<m:l+=1
    r-=1
    ans+=1
print ans

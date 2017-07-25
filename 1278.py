def bin_search(a,b):
    l,r,mid=a,n-1,0
    while l<=r:
        mid=(l+r)>>1
        if p[mid][0]>b:
            r=mid-1
        else:
            l=mid+1
    if p[mid][0]<=b:mid+=1
    if mid>=n:return n
    return mid


p=[]
ans=0
n=input()
for i in range(n):
    a,b=map(int,raw_input().split())
    p.append([a-b,a+b])

p.sort()
for i in range(n-1):
    ans+=n-bin_search(i+1,p[i][1])
print ans

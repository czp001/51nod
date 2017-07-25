def lower_bound(nums,target):
    low,high=0,len(nums)-1
    pos=len(nums)
    while low<high:
        mid=(low+high)/2
        if nums[mid]<target:
            low=mid+1
        else:#>=
            high=mid
            pos=high
    return pos

n,m=map(int,raw_input().split())
a,b=[0]*n,[0]*m
for i in range(m):
    a[i]=input()
    if i==0:b[i]=a[i]
    else:
        b[i]=max(b[i-1],a[i])
for i in range(m):
    x=input()
    if x<=a[0] or x>b[n-1]:continue
    pos=lower_bound(b,x)
    a[pos-1]+=1
    b[pos-1]=max(b[pos-1],a[pos-1])
for i in range(n):
    print a[i]

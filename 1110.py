n=input()
a,l=[],0
for i in range(n):
    x,w=map(int,raw_input().split())
    a.append([x,w])
    l=l+w
a.sort()
m=l//2
d,t=0,a[0][0]
for i in range(n):
    d=d+a[i][1]
    if d>m:
        t=a[i][0]
        break
ans=0
for i in range(n):
    ans=ans+abs(a[i][0]-t)*a[i][1]
print ans

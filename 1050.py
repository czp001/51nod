n=input()
a=[]
for i in range(n):
    a.append(input())
a=[0]+a
s1=[0]*(n+1)
s2=[0]*(n+1)
tot=sum(a)
da,xiao=-10**15,10**15
for i in range(1,n+1):
    s1[i]=max(s1[i-1]+a[i],a[i])
    da=max(da,s1[i])
    s2[i]=min(s2[i-1]+a[i],a[i])
    xiao=min(xiao,s2[i])
print max(da,tot-xiao)

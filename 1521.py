po=[0]*200010
n,k,a=map(int,raw_input().split())
m=input()
f,num=-1,(n+1)/(a+1)
b=map(int,raw_input().split())
for i in range(m):
    x=b[i]
    po[x]=1
    l=x-1
    while(l>=1 and po[l]==0):l-=1
    r=x+1
    while(r<=n and po[r]==0):r+=1
    num-=(r-l)/(a+1)-(r-x)/(a+1)-(x-l)/(a+1)
    if num<k and f==-1:
        f=i+1
        break
print f

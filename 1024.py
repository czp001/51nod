from math import log
m,n,a,b=list(map(int,input().split()))
s={}
for i in range(a,n+a):
    for j in range(b,b+m):
        s[i**j]=1
print(len(s))

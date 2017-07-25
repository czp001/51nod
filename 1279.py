n,m=map(int,raw_input().split())
s=[]
for i in range(n):
    j=input()
    if len(s)==0:s.append(j)
    else:
        s.append(min(s[-1],j))
ans=0
for i in range(m):
    p=input()
    while len(s)>0 and s[-1]<p:
        s.pop()
    if len(s)>0:
        ans+=1
        s.pop()
print ans

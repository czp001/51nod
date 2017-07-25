n=int(input())
l,t=[],1
for i in range(n):
    l.append(list(map(int,input().split())))
    t=t*l[i][0]
s=0
for i in range(n):
    s=s+l[i][1]*t//l[i][0]*pow(t//l[i][0],l[i][0]-2,l[i][0])
print(s%t)

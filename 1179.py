N=10**6+5
flag=[0]*N
m=0
n=input()
for i in range(n):
    t=input()
    flag[t]+=1
    m=max(m,t)
for i in range(m,0,-1):
    s=0
    for j in range(i,m+1,i):
        s+=flag[j]
        if s>=2:break
    if s>=2:break
print i

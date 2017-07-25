N=10**6+500
f,m,c=[0]*N,0,0
n=input()
w=map(int,raw_input().split())
for i in w:
    f[i]+=1
    m=max(m,i)
for i in range(m+100):
    if f[i]>1:
        f[i+1]+=f[i]//2
        f[i]%=2
    c+=f[i]
print c

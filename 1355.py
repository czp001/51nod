ans,p,nmax=1,10**9+7,1000001
fib=[0]*nmax
flag=[0]*nmax
cnt=[0]*nmax

fib[1]=1
for i in range(2,nmax):
    fib[i]=(fib[i-1]+fib[i-2])%p
n=input()
for i in range(n):
    a=input()
    flag[a]=1

for i in range(nmax-1,2,-1):
    j=2*i
    while(j<nmax and not flag[i]):
        flag[i]|=flag[j]
        j=j+i
    if(not flag[i]):
        continue
    cnt[i]=1
    j=i*2
    while(j<nmax):
        cnt[i]-=cnt[j]
        j=j+i
    t=cnt[i]%(p-1)
    if t:
        ans=ans*pow(fib[i],t,p)%p
print ans%p

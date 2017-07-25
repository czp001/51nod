N=10**6+200
prime=[0]*N
vst=[0]*N
num=0

for i in range(2,N):
    if(not vst[i]):
        prime[num]=i
        num+=1
    j=0
    while(prime[j]*i<N and j<num):
        vst[prime[j]*i]=1
        if(i%prime[j]==0):
            break
        j=j+1

n=int(input())
for i in range(0,N):
    if prime[i]>=n and i+1 in prime:
        print(prime[i])
        break

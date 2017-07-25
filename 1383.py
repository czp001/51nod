d=[0]*(10**6+5)
p=10**9+7
d[1]=1
for n in range(2,10**6+2):
    if n%2==0:
        d[n]=(d[n-1]+d[n//2])%p
    else:
        d[n]=d[n-1]%p
n=int(input())
print(d[n])

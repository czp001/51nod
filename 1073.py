n,k=list(map(int,input().split()))
a=0
for i in range(2,n+1):
    a=(a+k)%i
print(a+1)

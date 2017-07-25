N=10**5+5
a=[0]*N
a[1]=1
mx=[0]*N
mx[1]=1
for i in range(2,10**5+1):
    if i%2==0:
        a[i]=a[i//2]
    else:
        t=(i-1)//2
        a[i]=a[t]+a[t+1]
    mx[i]=max(a[i],mx[i-1])
n=input()
for i in range(n):
    m=input()
    print(mx[m])

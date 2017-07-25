from math import log
m=10**9+7
f=[0]*200
f[1]=1
for i in range(2,200):
    f[i]=f[i-1]+f[i-2]
t=int(input())
for i in range(t):
    n=int(input())
    if n==0:
        print(0)
    elif n<200:
        print((2**(int(log(f[n])/log(2))+1)-1)%m)
    else:
        k=int(n*log((1+5**0.5)/2)/log(2)-log(5**0.5)/log(2))+1
        print((pow(2,k,m)-1)%m)

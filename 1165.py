from fractions import gcd
a=[0]*(10**7+5)
for i in range(1,10**7+1,2):
    j,l,v=1,min(10**7//i-i,i-1),i*i+i
    while j<=l:
        if gcd(i,j)==1:a[v]=a[v]+1
        j+=2
        v+=2*i
for i in range(10**7,0,-1):
    if a[i]:
        j=2*i
        while j<=10**7:
            a[j]+=a[i]
            j+=i
t=int(input())
for i in range(t):
    n=int(input())
    print(a[n])

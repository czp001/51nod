from math import gcd
t=int(input())
for i in range(t):
    a,b,x,y=list(map(int,input().split()))
    if gcd(a,b)==gcd(x,y):
        print('Yes')
    else:
        print('No')

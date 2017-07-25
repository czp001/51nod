def gcd(a, b):
    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    while b != 0: 
        a, b = b, a%b
    return a
t=input()
for _ in range(t):
    a,b=map(int,raw_input().split())
    p=a+3*b
    q=4*(a+b)
    d=gcd(p,q)
    p=p//d
    q=q//d
    print str(p)+'/'+str(q)

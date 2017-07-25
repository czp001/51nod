def bezout(a,b):
    u,  v,  s,  t = 1, 0, 0, 1
    while b !=0:
        q, r = [(a-a%b)//b, a%b]
        a, b = b, r
        u, s = s, u - q*s
        v, t = t, v - q*t
    return [u, v, a]

def solve(n,a,b):
    ans=0
    xx,yy,d=bezout(a,b)
    z=a*b//d
    if (1+n)%d:return 0
    else:
        xx=xx*(1+n)//d
        r=b//d
        xx=xx%r
        if xx==0:xx=xx+r
        re=n-xx*a
        if re<0:return 0
        else:
            ans=ans+1
            ans=ans+re//z
    return ans
    
t=input()
for i in range(t):
    n,a,b=map(int,raw_input().split())
    print solve(n,a,b)

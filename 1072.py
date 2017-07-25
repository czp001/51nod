n=input()
for i in range(n):
    a,b=map(int,raw_input().split())
    if a>b:a,b=b,a
    c=b-a
    s=int((1+5**0.5)*c/2)
    if s==a:print 'B'
    else:print 'A'

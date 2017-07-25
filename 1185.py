from math import log10
def sq(n):
    x = 10**int(log10(n)/2)
    while not (x * x <= n and (x + 1) * (x + 1) > n) :
        x = int((x + n // x) // 2)
    return x
n=input()
for i in range(n):
    a,b=map(int,raw_input().split())
    if a>b:a,b=b,a
    c=b-a
    x=(c+sq(5*c*c))//2
    if x==a:print('B')
    else:print('A')

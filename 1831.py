def isprime(x):
    if x < 2:return 0
    t = int(x**0.5)
    for i in range(2,t+1):
        if x % i == 0:return 0
    return 1
    
t=input()
for i in range(t):
    n=input()
    f=0
    if isprime(n):
        if n==2 or n==17:f=1
    else:
        if n > 2 and n != 16 and n != 34 and n != 289:
            f=1
    if f:print 'TAK'
    else:print 'NIE'

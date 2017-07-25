a,b=map(int,raw_input().split())
def gcd(a, b):
    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    while b != 0: 
        a, b = b, a%b
    return a
print a*b/gcd(a,b)

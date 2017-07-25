def cycleLen(n):
    i = 1
    while not n%2: n/=2
    while not n%5: n/=5
    if n==1: return 0
    while True:
        if pow(10,i,n)==1: return i
        i+=1

n=input()
lmax=0
mn=0
for j in xrange(1,n+1):
    l=cycleLen(j)
    if l>lmax:
        lmax=l
        mn=j

print(mn)

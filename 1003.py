from math import log
n=input()
s=0
for i in xrange(1,int(log(n)/log(5))+1):
    s=s+n/5**i
print s

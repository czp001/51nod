from math import sqrt
n=input()
t=0
for i in xrange(0,int(sqrt(n/2))+1):
    j=int(sqrt(n-i*i))
    if(i*i+j*j==n):
        print i,j
        t=t+1
if(t==0):print 'No Solution'

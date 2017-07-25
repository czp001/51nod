from math import sqrt,log,exp,floor
T=input()
s=[]
for i in xrange(T):
    s.append(input())
for i in xrange(T):
    print int(floor(log(sqrt(2*3.1415926*s[i]))/log(10)+s[i]*log(s[i]/exp(1))/log(10))+1)

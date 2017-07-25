k,n=map(int,raw_input().split())
a=[]
for i in range(n):
    a.append(input())
a=sorted(a)
s=set(a)

t=0
for i in a:
    if k-i in s and i<k-i:
        print i, k-i
        t=t+1
if t==0:
    print 'No Solution'

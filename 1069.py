n=input()
a=[]
for i in range(n):
    a.append(input())
for i in range(1,n):
    a[i]=a[i]^a[i-1]
if(a[n-1]==0):
    print 'B'
else:
    print 'A'

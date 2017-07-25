l={1:1}
a,b=1,1
while a<=10**9:
    a,b=b,a+b
    l[b]=1
t=input()
for i in range(t):
    n=input()
    if n in l:
        print 'B'
    else:
        print 'A'

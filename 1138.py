n=input()
k=int(n**0.5)
t=0
i=2*k
while i>=2:
    if (2*n+i-i*i)%(2*i)==0 and (2*n+i-i*i)>0:
        print (2*n+i-i*i)//(i*2)
        t=t+1
    i=i-1
if t==0:
    print 'No Solution'

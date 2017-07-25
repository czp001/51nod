p,a=map(int,raw_input().split())
s=''
if (pow(a,(p-1)/2,p)==1):
    for i in xrange(1,p):
        if(pow(i,2,p)==a):
            s=s+(str(i)+' ')
    print s[0:-1]
else:
    print 'No Solution'

t=input()
while(t):
    n=input()
    x=int(((8*n+1)**0.5-1)/2)
    if n==1:
        print 1
    elif x*(x+1)//2+1==n:
        print 1
    else: 
        print 0
    t=t-1

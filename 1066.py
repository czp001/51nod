t=input()
for i in range(t):
    n,k=map(int,raw_input().split())
    if(n%(k+1)):
        print 'A'
    else:
        print 'B'

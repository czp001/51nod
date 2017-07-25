s,sm=[0]*10005,{}
n,k=map(int,raw_input().split())
for i in range(1,n+1):
    a=input()
    s[i]=s[i-1]+a
    sm[s[i]]=i

def solve(x):
    for i in range(n+1):
        if s[i]+k in sm:
            for j in range(i,n+1):
                if s[j]-s[i]==x:
                    print "%d %d\n"%(i+1,j)
                    return
    print 'No Solution'             
    return 
solve(k)

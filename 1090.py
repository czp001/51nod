n=input()
k=[]

for i in range(n):
    k.append(input())

k.sort()

def solve():
    f=0
    for a in range(n):
        for b in range(a+1,n):
            if(-k[a]-k[b] in k[b+1:]):
                print k[a],k[b],-k[a]-k[b]
                f=1
    if(f==0):print 'No Solution'
    
if __name__=='__main__':
    solve()

n=input()
a=[[0]*n for i in range(n)]
b=[[0]*n for i in range(n)]
for i in xrange(n):
    a[i]=map(int,raw_input().split())

for i in xrange(n):
    b[i]=map(int,raw_input().split())

def mat_mult(A, B):
    C = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
    return C

c=mat_mult(a,b)
for i in xrange(n):
    s=str(c[i][0])
    for j in xrange(1,n):
        s=s+' '+str(c[i][j])
    print s

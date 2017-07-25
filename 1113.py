n,m=map(int,raw_input().split())
a=[[0]*n for i in range(n)]
p=10**9+7
for i in xrange(n):
    a[i]=map(int,raw_input().split())

def mat_mult(A, B, m):
    C = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= m
    return C

def mat_pow(A, p, m):
    if p == 1:
        return A
    if p % 2:
        return mat_mult(A, mat_pow(A, p-1, m), m)
    X = mat_pow(A, p//2, m)
    return mat_mult(X, X, m)

c=mat_pow(a,m,p)
for i in xrange(n):
    s=str(c[i][0])
    for j in xrange(1,n):
        s=s+' '+str(c[i][j])
    print s

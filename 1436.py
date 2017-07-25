def fib(n, m):
    T = [[1,1], [1,0]]
    if n == 0:
        return 0
    if n==1:
        return 1
    T = mat_pow(T, n-1, m)
    return T[0][0]
    
def mat_mult(A, B, m):
    C = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= m
    return C

def mat_pow(A, p, m):
    if p==0:return [[1,0],[0,1]]
    if p == 1:
        return A
    if p % 2:
        return mat_mult(A, mat_pow(A, p-1, m), m)
    X = mat_pow(A, p//2, m)
    return mat_mult(X, X, m)

def ans(n,k,l,m):
    if 2**l<=k:return 0
    else:c=list(bin(k))[2:].count('1')
    f1=fib(n+2,m)
    f2=pow(2,n,m)-f1
    return pow(f1,l-c,m)*pow(f2,c,m)%m
    
n,k,l,m=map(int,raw_input().split())
print ans(n,k,l,m)

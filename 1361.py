def loop(p):
    if pow(117,(p-1)>>1,p)==1:
        return p-1
    return p+1
def b(n, p):
    i=(p+1)//2
    T = [[11*i%p,3*i%p], [39*i%p,11*i%p]]
    n=pow(2,n,loop(p))
    T = mat_pow(T, n, p)
    return (T[0][0]+T[1][1])
    
def mat_mult(A, B, p):
    C = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= p
    return C

def mat_pow(A, p, m):
    if p==0:return [[1,0],[0,1]]
    if p == 1:
        return A
    if p % 2:
        return mat_mult(A, mat_pow(A, p-1, m), m)
    X = mat_pow(A, p//2, m)
    return mat_mult(X, X, m)

def a(n,p):
    return (b(n-1,p)-5)*pow(6,p-2,p)%p

t=input()
for i in range(t):
    n,p=map(int,raw_input().split())
    if p==2 or p==3:print(1)
    else:print(a(n,p))

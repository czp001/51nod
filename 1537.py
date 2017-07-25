def xy(n, m):
    T = [[1,2], [1,1]]
    if n == 1:
        return [1,1]
    else:
        T = mat_pow(T, n-1, m)
        return [sum(T[0])%m,sum(T[1])%m]
    
def mat_mult(A, B, m):
    C = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
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
m=10**9+7    
n=int(input())
[x,y]=xy(n,m)
print((x*x+2*y*y+1)*500000004%m)

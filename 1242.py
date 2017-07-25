def fib(n, m):
    T = [[1,1], [1,0]]
    if n == 1:
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
    if p == 1:
        return A
    if p % 2:
        return mat_mult(A, mat_pow(A, p-1, m), m)
    X = mat_pow(A, p//2, m)
    return mat_mult(X, X, m)
    
n=input()
print fib(n,1000000009)

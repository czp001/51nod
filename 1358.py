def fib(n, m):
    T = [[0] * 34 for i in range(34)]
    T[0][9]=1
    T[0][33]=1
    for i in range(1,34):
        T[i][i-1]=1
    if n <= 4:
        return 1
    T = mat_pow(T, (n-4)*10, m)
    return sum(T[0])%m
    
def mat_mult(A, B, m):
    C = [[0] * 34 for i in range(34)]
    for i in range(34):
        for j in range(34):
            for k in range(34):
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
    
n=int(input())
print(fib(n,10**9+7))

mod=10**9+7
def s(p,q,r,n):
    s0=[0,3*r*pow(q,n,mod)%mod,0]
    q=pow(q,mod-2,mod)
    T = [[p*q%mod,q,0], [0,q,0],[p*q%mod,q,1]]
    T ,ans= mat_pow(T, n, mod),0
    for i in range(3):
        ans=ans+T[2][i]*s0[i]
    return ans%mod
    
def mat_mult(A, B, mod):
    C = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k]*B[k][j]
            C[i][j] %= mod
    return C

def mat_pow(A, n, mod):
    if n==0:return [[1,0,0],[0,1,0],[0,0,1]]
    if n == 1:
        return A
    if n % 2:
        return mat_mult(A, mat_pow(A, n-1, mod), mod)
    X = mat_pow(A, n//2, mod)
    return mat_mult(X, X, mod)

p,q,r,n=map(int,raw_input().split())    
print s(p,q,r,n)

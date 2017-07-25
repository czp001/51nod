def contfrac(n):
    cf=[]
    s=int(n**0.5)
    m0,d0,a0=0,1,s
    cf.append(a0)
    m1=d0*a0-m0
    d1=(n-m1*m1)//d0
    a1=(s+m1)//d1
    cf.append(a1)
    while a1!=2*s:
        m0,d0,a0=m1,d1,a1
        m1=d0*a0-m0
        d1=(n-m1*m1)//d0
        a1=(s+m1)//d1
        cf.append(a1)
    return cf

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

n,k=map(int,raw_input().split())
mod=10**9+7
k=k+1
frac=contfrac(n)
Len=len(frac)-1
remain,loop=k%Len,k//Len
mp,mr=[[1,0],[0,1]],[[1,0],[0,1]]
for i in range(Len,0,-1):
    A=[[frac[i],1],[1,0]]
    mp=mat_mult(mp,A,mod)
mp=mat_pow(mp,loop,mod)
for i in range(remain,0,-1):
    A=[[frac[i],1],[1,0]]
    mr=mat_mult(mr,A,mod)
ma=mat_mult(mr,mp,mod)
p,q=ma[1][0]%mod,ma[1][1]%mod
t,q=q,p
p=(frac[0]*p+t)%mod
print "%d/%d"%(p,q)

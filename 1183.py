def edd(a,b):
    n,m=len(a),len(b)
    f=[[0]*(m+5) for i in range(n+5)]
    for i in range(n+1):
        f[i][0]=i
    for j in range(m+1):
        f[0][j]=j

    for i in range(1,1+n):
        for j in range(1,m+1):
            if a[i-1]==b[j-1]:
                f[i][j]=f[i-1][j-1]
            else:
                f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
    return f[n][m]

s1=input()
s2=input()
print(edd(s1,s2))

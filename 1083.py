a=[]
n=input()
for i in range(n):
    a=a+[map(int,raw_input().split())]
f=[[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            f[i][j]=a[0][0]
        elif i==0 and j!=0:
            f[i][j]=f[i][j-1]+a[i][j]
        elif j==0 and i!=0:
            f[i][j]=f[i-1][j]+a[i][j]
        else:
            f[i][j]=max(f[i-1][j],f[i][j-1])+a[i][j]
print(f[n-1][n-1])

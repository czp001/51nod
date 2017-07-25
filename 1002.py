n=input()
a=[]
m=[[0]*505 for i in range(505)]
for i in range(n):
        a=a+[map(int,raw_input().split())]

for i in range(n):
    for j in range(i+1):
        if i==0 and j==0:
            m[i][j]=a[i][j]
        elif j==0 and i!=0:
            m[i][j]=m[i-1][j]+a[i][j]
        elif i==j and i>0 and j>0:
            m[i][j]=m[i-1][j-1]+a[i][j]
        else:
            m[i][j]=max(m[i-1][j],m[i-1][j-1])+a[i][j]
print(max(m[n-1]))

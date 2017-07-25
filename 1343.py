n,m=map(int,raw_input().split())
a=[]
for i in range(n):
    a.append(list(map(int,raw_input().split())))
def det(a):
    ans=1
    for i in range(n):
        for j in range(i+1,n):
            while a[j][i]!=0:
                t=a[i][i]//a[j][i]
                for k in range(i,n):
                    a[i][k]=(a[i][k]-a[j][k]*t)%m
                    a[i][k],a[j][k]=a[j][k],a[i][k]
                ans*=-1
        if a[i][i]==0:
            return 0
        else:
            ans=ans*a[i][i]%m
    return ans%m

print(det(a)%m)

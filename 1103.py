N=50005
flag=[-1]*N
s=[0]*N
a=[0]*N

n=int(input())
for i in range(1,n+1):
    a[i]=int(input())
for i in range(1,n+1):
    s[i]=(s[i-1]+a[i])%n
    if s[i]==0:
        print(i)
        for j in range(1,i+1):
            print(a[j])
        break
    else:
        if flag[s[i]]==-1:
            flag[s[i]]=i
        else:
            print(i-flag[s[i]])
            for j in range(flag[s[i]]+1,i+1):
                print(a[j])
            break

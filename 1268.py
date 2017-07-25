n,k=map(int,raw_input().split())
a=[]
for i in range(n):
    a.append(int(input()))

def dfs(i,sum):
    if i==n:return sum==k;
    if (dfs(i+1,sum)):return True
    if (dfs(i+1,sum+a[i-1])):return True
    else:False


if (dfs(0,0)):
    print('Yes')
else:
    print('No')

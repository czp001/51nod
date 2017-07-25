N=10**4+1
dp=[[0]*20 for i in range(N)]
mm=[0]*N
def initRMQ(n,b):
    mm[0]=-1
    for i in range(1,n+1):
        if i & (i - 1) == 0:
            mm[i]=mm[i - 1] + 1
        else:
            mm[i]=mm[i - 1]
        dp[i][0]=b[i]
    for j in range(1,mm[n]+1):
        i=1
        while i + (1 << j) - 1 <= n:
            dp[i][j] = max(dp[i][j - 1], dp[i + (1 << (j - 1))][j - 1])
            i+=1

def RMQ(x,y):
    k=mm[y-x+1]
    return max(dp[x][k], dp[y - (1 << k) + 1][k])

b=[0]*N
n=int(input())
for i in range(1,n+1):
    b[i]=int(input())
initRMQ(n,b)
Q = int(input())
for i in range(Q):
    l,r = map(int,raw_input().split())
    print(RMQ(l+1,r+1))

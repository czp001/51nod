MAX=50010
h=[0]*MAX
L=[0]*MAX
R=[0]*MAX
st=[0]*MAX
def solve():
    t=0
    for i in range(n):
        while t>0 and h[st[t-1]]>=h[i]:t=t-1
        if t==0:L[i]=0
        else:L[i]=st[t-1]+1
        st[t]=i
        t=t+1
    t=0
    for i in range(n-1,-1,-1):
        while t>0 and h[st[t-1]]>=h[i]:t=t-1
        if t==0:R[i]=n
        else:R[i]=st[t-1]
        st[t]=i
        t=t+1
    res=0
    for i in range(n):
        res=max(res,h[i]*(R[i]-L[i]))
    print(res)
n=input()
for i in range(n):
    h[i]=input()
solve()

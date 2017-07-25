N=101
fact=[0]*N
f=[[0]*N for i in range(2)]
pre=[0]*N
suf=[0]*N
def value(x):
    if x<deg:
        return f[cur][x]
    pre[0]=x
    for i in range(1,deg):
        pre[i]=pre[i-1]*(x-i)
    suf[deg-1]=x-deg+1
    for i in range(deg-2,-1,-1):
        suf[i]=suf[i+1]*(x-i)
    ret=0
    for i in range(deg):
        tmp=f[cur][i]
        if i>0:
            tmp=tmp*pre[i-1]
        if i<deg-1:
            tmp=tmp*suf[i+1]
        tmp=tmp//fact[i]//fact[deg-1-i]
        if ((deg - 1 - i) & 1) == 1:
            ret=ret-tmp
        else:
            ret=ret+tmp
    return ret

val=int(input())
cur,nxt,deg=0,1,1
f[cur][0],fact[0]=1,1
while (val>1)>0:
    pos=val%2
    for i in range(0,deg+1):
        if i>0:
            f[nxt][i]=f[nxt][i-1]+value(pos)
        else:
            f[nxt][i]=value(pos)
        pos+=2
    fact[deg]=fact[deg-1]*deg
    deg+=1
    cur^=1
    nxt^=1
    val>>=1
print(value(1))

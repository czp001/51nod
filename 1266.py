n,L=map(int,raw_input().split())
x=[]
for i in range(n):
    a=int(raw_input())
    x.append(a)


mint,maxt=0,0
for i in range(n):
    mint=max(mint,min(x[i],L-x[i]))
    maxt=max(maxt,max(x[i],L-x[i]))

print mint,maxt

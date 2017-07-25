x,y,z=[],[],[]
n=input()
for i in range(n):
    a,b,c=map(int,raw_input().split())
    x.append(a)
    y.append(b)
    z.append(c)
x.sort()
y.sort()
z.sort()
m=n//2
s=0
for i in range(n):
    s=s+abs(x[m]-x[i])+abs(y[m]-y[i])+abs(z[m]-z[i])
print s

n=input()
p=[0]*(n+5)
p[1]=1
for i in range(2,n+1):
    p[i]=p[i-1]*2.*(i-1)/(2*i-1.0)
print '%.6f'%p[n]

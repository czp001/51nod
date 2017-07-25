n=input()
a=[]
for i in range(n):
    a.append(input())
a.sort()
if n%2:m=a[(n-1)//2]
else:m=(a[n//2]+a[n//2-1])//2
s=0
for i in range(n):
    s=s+abs(m-a[i])
print s

n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
n1=a.count(1)
n2=a.count(2)
l=len(a)
print((n1-1)*n1+n2*(n2-1)//2+(l-n1)*n1)

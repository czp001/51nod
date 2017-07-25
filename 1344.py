n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

mm=10**10
s=0
for i in a:
    s+=i
    if(s<mm):mm=s
print (-mm)

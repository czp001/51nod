N=50010
a=[0]*N
s=[0]*N
q1=[0]*N
q2=[0]*N
n=int(input())
for i in  range(1,n+1):
    a[i]=int(input())
    s[i]=s[i-1]+a[i]
qq=int(input())
for j in range(1,qq+1):
    q1[j],q2[j]=list(map(int,input().split()))
for j in range(1,qq+1):    
    print(s[q1[j]+q2[j]-1]-s[q1[j]-1])

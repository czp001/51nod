n=input()
a=[[0]*n for i in range(n)]
b=[[0]*n for i in range(n)]
c=[[0]*n for i in range(n)]
for i in range(n):
    a[i]=map(int,raw_input().split())

for i in range(n):
    b[i]=map(int,raw_input().split())
    
for i in range(n):
    c[i]=map(int,raw_input().split())

s=range(n)

def mult(v, A):
    C = [0]*n
    for i in range(n):
        for j in range(n):
                C[i]+= A[j][i]*v[j]
    return C

if mult(mult(s,a),b)==mult(s,c):print 'Yes'
else:print 'No'

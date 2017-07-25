def det(t):
    if(t[0][0]*t[1][1]*t[2][2]+t[0][1]*t[1][2]*t[2][0]+t[0][2]*t[1][0]*t[2][1]\
       -t[0][0]*t[1][2]*t[2][1]-t[0][1]*t[1][0]*t[2][2]-t[0][2]*t[1][1]*t[2][0]==0):
        return 'Yes'
    else:
        return 'No'
    
def mat(a,b,c,d):
    m,mm=[],[b,c,d]
    for i in mm:
        m.append([a[0]-i[0],a[1]-i[1],a[2]-i[2]])    
    return m
n=int(input())
l=[]
for i in range(n*4):
    l.append(list(map(int,input().split())))

for i in range(n):
    print(det(mat(l[0+4*i],l[1+4*i],l[2+4*i],l[3+4*i])))

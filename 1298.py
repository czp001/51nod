class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

def distance(pa,pb):
    return (pa.x-pb.x)**2+(pa.y-pb.y)**2

def bananapo(pa,pb,po):
    if pa.x==pb.x:
        a,b,c=1,0,-pa.x
    elif pa.y==pb.y:
        a,b,c=0,1,-pa.y
    else:
        a=pa.y-pb.y
        b=pb.x-pa.x
        c=pa.x*pb.y-pa.y*pb.x
    ds1=(a*po.x+b*po.y+c)**2
    ds2=(a*a+b*b)*r*r
    if ds1>ds2:
        return 0
    ang1=(po.x-pa.x)*(pb.x-pa.x)+(po.y-pa.y)*(pb.y-pa.y)
    ang2=(po.x-pb.x)*(pa.x-pb.x)+(po.y-pb.y)*(pa.y-pb.y)
    if ang1>0 and ang2>0:
        return 1
    return 0

def is_intersected(a,b,c,o,r):
    disa=distance(o,a)
    disb=distance(o,b)
    disc=distance(o,c)
    r2=r*r
    if disa<r2 and disb<r2 and disc<r2:
        return 0
    elif disa>r2 and disb>r2 and disc>r2:
        return bananapo(a,b,o) or bananapo(a,c,o) or bananapo(b,c,o)
    return 1


t=input()
shuju=[]
for _ in range(4*t):
    shuju.append(map(int,raw_input().split()))
for i in range(t):
    ox,oy,r=shuju[4*i]
    ax,ay=shuju[4*i+1]
    bx,by=shuju[4*i+2]
    cx,cy=shuju[4*i+3]
    A, B = Point(ax,ay), Point(bx,by)
    C, O = Point(cx,cy), Point(ox,oy)
    if is_intersected(A,B,C,O,r):
        print "Yes"
    else:
        print "No"

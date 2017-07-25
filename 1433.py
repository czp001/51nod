n=input()
a=map(int,raw_input().split())
n0=a.count(0)
n5=a.count(5)
if n0==0:
    print '-1'
elif n5<9:
    print '0'
else:
    t=n5-n5%9
    print '5'*t+'0'*n0

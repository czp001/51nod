from sys import stdin
for i in stdin:
    l=len(i.strip())
    if l%2:
        print 'No'
    elif i.strip()[0:l//2]==i.strip()[l//2:]:
        print 'Yes'
    else:
        print 'No'

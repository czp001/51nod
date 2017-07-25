def merge(a):
    if len(a) <= 1:
        return 0

    h = len(a) / 2
    l, r = a[:h], a[h:]
    s = merge(l) + merge(r)

    j = 0
    for i in xrange(len(l)):
        while j < len(r) and r[j] < l[i]:
            j += 1
        s += j
    a.sort()
    return s

a=[]
n=input()
for i in range(n):
    a.append(input())
print merge(a)

s='abcdefghijklmnopqrstuvwxyz'
a=raw_input()
a=a.lower()
l=[]
for i in s:
    l.append(a.count(i))
l.sort()
w=0
for i in range(26):
    w=w+l[i]*(i+1)
print(w)

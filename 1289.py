N=100005
a=[0]*N
s,ans=[],0
t=input()
for i in range(t):
    a[i],dr=map(int,raw_input().split())
    if dr:
        s.append(a[i])
    else:
        while len(s):
            if a[i]>s[-1]:
                ans+=1
                s.pop()
            else:
                ans+=1
                break
print t-ans

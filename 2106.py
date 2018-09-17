n=input()
s={}
for i in range(n):
    a=input()
    if a in s:s[a]+=1
    else:s[a]=1
for i in s:
    if s[i]%2==1:
        print i
        break

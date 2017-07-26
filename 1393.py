N=1000010
a=[0]*N
s=[0]*N
t={}
string=raw_input()
l=len(string)
for i in range(l):
    if string[i]=='0':a[i+1]=-1
    else:a[i+1]=1
for i in range(1,l+1):
    s[i]=s[i-1]+a[i]
ans=0
for i in range(1,l+1):
    if s[i]==0:ans=max(ans,i)
    else:
        if s[i] not in t:
            t[s[i]]=i
        else:ans=max(ans,i-t[s[i]])
print ans

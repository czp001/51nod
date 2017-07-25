a,n=raw_input().split()
n=int(n)
while a[-1]=='0':
    a=a[:-1]
if a[-1]=='.':
    print int(a[:-1])**n
else:
    ido=a.index('.')
    lz=len(a)-1-ido
    if int(a[:ido])!=0:
        ans=str(int(a[:ido]+a[ido+1:])**n)
    else:
        ans=str(int(a[ido+1:])**n)
    bl=lz*n-len(ans)
    if bl>0:
        ans='.'+'0'*bl+ans
        print ans
    else:
        bl=-bl
        ans=ans[:bl]+'.'+ans[bl:]
        print ans

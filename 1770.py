def solve(a,b,d,n):
    if(n<=10):
        num=a*b*(10**n-1)/9
        return list(str(num)).count(str(d))
    else:
        s={}
        str3=111*a*b%10**3
        s[str3%10]=1
        str2=(str3-str3%10)/10%10
        if(str2 in s):
            s[str2]=s[str2]+1
        else:
            s[str2]=1
        str1=(str3-str3%100)/100
        if(str1 in s):
            s[str1]=s[str1]+n-2
        else:
            s[str1]=n-2
        k=(a*b+a*b/10)/10
        if(k!=0):
            if(k in s):
                s[k]=s[k]+1
            else:
                s[k]=1
        if(d in s):
            return s[d]
        else:
            return 0

t=input()
while(t):
    a,b,d,n=map(int,raw_input().split())
    t=t-1
    print(solve(a,b,d,n))

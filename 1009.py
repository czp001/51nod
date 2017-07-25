def one(n):
    cnt,i=0,1
    cur,after,before=0,0,0
    while n//i !=0:
        cur=(n/i)%10
        before=n/(i*10)
        after=n-(n/i)*i
        if(cur>1):
            cnt+=(before+1)*i
        if(cur<1):
            cnt+=before*i
        if(cur==1):
            cnt+=before*i+after+1
        i*=10;
    return cnt
n=input()
print one(n)

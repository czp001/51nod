s=[0]*(10**6+10)
for i in range(1,10**6+5):
    if i%7==0 or '7' in str(i):
        s[i]=s[i-1]
    else:
        s[i]=s[i-1]+i*i
t=input()
for i in range(t):
    n=input()
    print s[n]

n=int(input())
p=10**9+7
a,b=1,2
if n==1:
    print(a)
elif n==2:
    print(b)
else:
    for i in range(n-2):
        a,b=b%p,(a+b)%p
    print(b)

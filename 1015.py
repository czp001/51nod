def shui(n):
    lt,t=[],n
    while n:
        lt.append(n%10)
        n=n//10
    l=len(lt)
    s=0
    for i in lt:
        s=s+i**l
    if s==t:
        return 1
    else:
        return 0

m=input()
while not shui(m):
    m=m+1
print m

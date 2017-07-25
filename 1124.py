def a(n):
    r=1
    while n>0:
        r*=pow(4,n//10%2,10)*[1,1, 2, 6, 4, 2, 2, 4, 2, 8][n%10]
        n=n//5
    return r%10
n=input()
print a(n)

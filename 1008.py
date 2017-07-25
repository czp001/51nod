a, b = map(int,raw_input().split())  
s=1
for i in range(1,a+1):
    s=(s*i)%b
print s

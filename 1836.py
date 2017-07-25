from decimal import *
getcontext().prec = 25
t=input()
for i in range(1,t+1):
	n,m=map(int,raw_input().split())
	q=Decimal(n-1)/Decimal(n)
	ans=(Decimal(1)-q**m)/Decimal(1-q)
	print ans

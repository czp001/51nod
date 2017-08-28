#include <cstdio>
#include <bits/stdc++.h>
#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;
typedef long long LL;
const int mod=1e9+7;
const int p=1e9+7;
const int MOD = 1000000007;
struct Matrix
{
	int num1, num2;
	bool operator == (const Matrix &x) const
	{
		return num1 == x.num1 && num2 == x.num2;
	}
	Matrix operator * (const Matrix &x) const
	{
		return (Matrix){((LL)num1 * x.num1 + (LL)num2 * x.num2) % p,
		((LL)num1 * x.num2 + (LL)num2 * (x.num1 + x.num2)) % p};
	}
	Matrix pow(int k)
	{
		Matrix ret = (Matrix){1, 0}, tmp = *this;
		while(k)
		{
			if(k & 1)
				ret = ret * tmp;
			tmp = tmp * tmp;
			k >>= 1;
		}
		return ret;
	}
} A = {0, 1}, I = {1, 0};

LL getFun(LL n){
	return A.pow(n).num2;
}


//计算F(m - 1) * F(n % m) mod F(m)
LL getRes(LL n, LL m)
{
	LL k = n % m;
	if(k & 1)
		return getFun(m - k);
	return ((getFun(m) - getFun(m - k)) % MOD + MOD) % MOD;
}

LL Solve(LL n, LL m)
{
	LL t1 = n / m;
	if(m & 1)
	{
		LL t2 = t1 >> 1;
		if(t1 % 2 == 0 && t2 % 2 == 0)
			return getFun(n % m);
		if(t1 % 2 == 0 && t2 % 2 == 1)
			return ((getFun(m) - getFun(n % m)) % MOD + MOD) % MOD;
		if(t1 % 2 == 1 && t2 % 2 == 0)
			return getRes(n, m);
		if(t1 % 2 == 1 && t2 % 2 == 1)
			return ((getFun(m) - getRes(n, m)) % MOD + MOD) % MOD;
	}
	else
	{
		if(t1 & 1)
			return getRes(n, m);
		else
			return getFun(n % m);
	}
}

LL getResponse(LL n, LL m)
{
//	n += 2;
	LL res = Solve(n, m);
//	if(res == 0)
//		return getFun(m) - 1;
//	return res - 1;
	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	while(T--)
	{
		LL n, k;
		scanf("%lld %lld", &n, &k);
		printf("%lld\n", getResponse(n, k));
	}
	return 0;
}

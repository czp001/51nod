#include<bits/stdc++.h>
using namespace std;
struct xian
{
	int s,e;
}a[10005];
bool cmp(xian x, xian y)
{
	if (x.e == y.e)
	{
		return x.s>y.s;
	}
	return x.e<y.e;
}
int main(void)
{
	int n, s=1;
	cin>>n;
	for (int i=0; i<n; i++)
	{
		cin>>a[i].s>>a[i].e;
	}
	sort(a,a+n,cmp);
	for (int i=1; i<n; i++)
	{
		if (a[i].e==a[i-1].e || a[i].s<a[i-1].e)
		{
			a[i]=a[i-1];
		}
		else
		{
			s++;
		}
	}
	cout<<s;
	return 0;
}

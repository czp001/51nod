#include<iostream>
using namespace std;

const int N=50005;
const int mod=1000000007;
long long p[N];

long long q(long long n)
{
	return (3*n*n + 2*n + (n%2) * (2*n + 1)) / 8;
}

int a(int n)
{
    if((n%4-1)==0 || (n%4-1)==1)return 1;
    else return -1;/*
	switch(n%4-1)
	{
		case 0:return 1;
		case 1:return 1;
		case 2:return -1;
		case 3:return -1;
	}*/
}

int main()
{
	p[0]=1;
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		long long sum=0;
		int j=1;
		while(i-q(j)>=0)
		{
			if(a(j)>0)
			{
				sum+=p[i-q(j)]%mod;
			}
			else sum=(sum-p[i-q(j)])%mod;
			if(sum<0)sum=sum+mod;
			j++;
		}
		p[i]=sum%mod;
	}
	cout<<p[n];
}

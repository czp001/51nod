#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
typedef long long LL;
const int N=1000005;
int n, m;
LL ans,mod=1000000007;
LL fac[N],invf[N];
LL modpow(LL x, LL k)
{
	int ret = 1;
	for( ; k > 0; k >>= 1, x = (LL)x * x % mod)
		if(k & 1)
			ret = (LL)ret * x % mod;
	return ret;
}

LL C(LL n,LL m)
{
    return fac[n]*invf[m]%mod*invf[n-m]%mod;
}

int main()
{
    fac[0]=1;
    invf[0]=1;
    for(int i=1;i<N;i++){fac[i]=i*fac[i-1]%mod;}
    invf[N-1]=modpow(fac[N-1],mod-2);
    for(int i=N-2;i>0;i--)invf[i]=invf[i+1]*(i+1)%mod;
	cin>>n>>m;
	if(m>n)
	{
		cout<<0<<endl;;
		return 0;
	}
    ans=0;
    for(int k=0;k<=m-1;k++)
    {
        if(k%2==0)ans=ans+C(m,k)*modpow(m-k,n)%mod;
        else{ans=(mod+ans-C(m,k)*modpow(m-k,n)%mod);}
    }
    ans=(mod+ans)%mod;
	cout<<ans<<endl;
	return 0;
}

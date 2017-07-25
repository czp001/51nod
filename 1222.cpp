#include<iostream>
using namespace std;
const int N=320000;
typedef long long LL;

int tot,p[N],mu[N+5];
LL a,b,ans;
bool bz[N+5];


void init()
{
    mu[1]=1;
    for (int i=2;i<=N;i++)
    {
        if (!bz[i])
        {
            mu[i]=-1; p[tot++]=i;
        }
        for (int j=0;j<tot;j++)
        {
            int I=i*p[j];
            if (I>N) break;
            bz[I]=1;
            if (i%p[j]==0)
            {
                mu[I]=0; break;
            }
            mu[I]=-mu[i];
        }
    }
}

LL calc(LL n)
{
    if (!n) return 0;
    ans=0;
    for (int k=1;(LL)k*k<=n;k++) if (mu[k]!=0)
    {
        LL m=n/((LL)k*k),s=0;
        for (int i=1;(LL)i*i*i<=m;i++)
        {
            for (int j=i+1;(LL)i*j*j<=m;j++)
            {
                s+=(m/((LL)i*j)-j)*6+3;
            }
            s+=(m/((LL)i*i)-i)*3+1;
        }
        if (mu[k]==1) ans+=s;else ans-=s;
    }
    return (ans+n)/2;
}

int main()
{
    init();
    cin>>a>>b;
    cout<<calc(b)-calc(a-1);
    return 0;
}

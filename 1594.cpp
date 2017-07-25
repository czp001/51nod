#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int N=2e6+1;

typedef long long LL;

int T,n,tot,p[N],phi[N],mu[N];

LL ans,s[N],f[N];

bool bz[N];

void work()
{
    scanf("%d",&n);
    ans=tot=0;
    memset(bz,0,sizeof(bz));
    memset(phi,0,sizeof(phi));
    memset(mu,0,sizeof(mu));
    memset(s,0,sizeof(s));
    memset(f,0,sizeof(f));
    mu[1]=phi[1]=1;
    for (int i=2;i<=n;i++)
    {
        if (!bz[i])
        {
            p[tot++]=i; mu[i]=-1; phi[i]=i-1;
        }
        for (int j=0;j<tot;j++)
        {
            int k=i*p[j];
            if (k>n) break;
            bz[k]=1;
            if (i%p[j]==0)
            {
                mu[k]=0;
                phi[k]=phi[i]*p[j];
                break;
            }
            mu[k]=-mu[i];
            phi[k]=phi[i]*(p[j]-1);
        }
    }
    for (int i=1;i<=n;i++) s[phi[i]]++;
    for (int i=1;i<=n;i++)
        for (int j=i;j<=n;j+=i) f[i]+=s[j];
    for (int i=1;i<=n;i++) f[i]=f[i]*f[i];
    for (int i=1;i<=n;i++) if (mu[i]!=0)
        for (int d=1;i*d<=n;d++) ans+=mu[i]*phi[d]*f[i*d];
    printf("%lld\n",ans);
}

int main()
{
    for (scanf("%d",&T);T--;work());
    return 0;
}

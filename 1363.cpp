#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define mod 1000000007
#define inf 999999999
#define esp 0.00000000001
ll scan()
{
    ll res = 0 , ch ;
    while( !( ( ch = getchar() ) >= '0' && ch <= '9' ) )
    {
        if( ch == EOF ) return 1 << 30 ;
    }
    res = ch - '0' ;
    while( ( ch = getchar() ) >= '0' && ch <= '9' )
        res = res * 10 + ( ch - '0' ) ;
    return res ;
}
const int MAXN=32000;
int fa[100];
int si[100],p;
ll ans;
int prime[MAXN],cnt;
bool vis[MAXN];
inline int Prime(int n)
{
    cnt=0;
    memset(vis,0,sizeof(vis));
    for(int i=2;i<n;i++)
    {
        if(!vis[i])
        prime[cnt++]=i;
        for(int j=0;j<cnt&&i*prime[j]<n;j++)
        {
            vis[i*prime[j]]=1;
            if(i%prime[j]==0)
            break;
        }
    }
    return cnt;
}
inline void dfs(ll fac,ll pos,ll x,ll oula)
{
    if(pos==p)
    {
        ans+=oula*fac/2;
        ans%=mod;
        return;
    }
    ll base=1;
    ll hh=1;
    for(int i=0;i<=si[pos];i++)
    {
        dfs(fac*base,pos+1,x,oula*hh);
        base*=fa[pos];
        hh*=fa[pos]-(i==0?1:0);
    }
}
int main()
{
    ll x,y,z,i,t;
    Prime(MAXN);
    int T;
    scanf("%d",&T);
    while(T--)
    {
        memset(si,0,sizeof(si));
        scanf("%lld",&x);
        ans=0;
        p=0;
        z=x;
        for(i=0;i<cnt&&prime[i]*prime[i]<=z;i++)
        {
            if(z%prime[i]==0)
            {
                fa[p]=prime[i];
                while(z%prime[i]==0)
                {
                    z/=prime[i];
                    si[p]++;
                }
                p++;
            }
        }
        if(z>1)
        {
            fa[p]=z;
            si[p++]++;
        }
        dfs(1,0,x,1);
        printf("%lld\n",(x*(ans+1))%mod);
    }
    return 0;
}

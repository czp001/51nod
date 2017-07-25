#include <iostream>
#include <cstring>

using namespace std;
typedef long long LL;
const LL MAXN = 5000010;

bool flag[MAXN];
LL phi[MAXN];
LL p[MAXN];
LL cnt = 0;
void Phi()
{
    cnt = 0;
    memset(flag, true, sizeof(flag));
    phi[1] = 1;
    for(LL i=2; i<MAXN; i++)
    {
        if(flag[i])
        {
            p[cnt++] = i;
            phi[i] = i-1;
        }
        for(LL j=0; j<cnt; j++)
        {
            if(i*p[j] > MAXN)
                break;
            flag[i*p[j]] = false;
            if(i%p[j] == 0)
            {
                phi[i*p[j]] = p[j] * phi[i];
                break;
            }
            else
                phi[i*p[j]] = (p[j]-1) * phi[i];
        }
    }
}
LL ans[MAXN];
void Init()
{
    Phi();
    memset(ans, 0, sizeof(ans));
    for(LL i=1; i<MAXN; i++)
        for(LL j=2; j<MAXN; j++)
            if(i*j < MAXN)
                ans[i*j] += phi[j]*i;
            else
                break;
    for(LL i=1; i<MAXN; i++)
        ans[i] += ans[i-1];
}
int main()
{
    Init();
    LL T, N;
    cin>>T;
    while(T--)
    {
        cin>>N;
        cout<<ans[N]<<endl;
    }
    return 0;
}

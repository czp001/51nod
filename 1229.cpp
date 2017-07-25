#include <iostream>  
#include <string.h> 
  
using namespace std;  
typedef long long LL;  
const int N = 2005;  
const LL MOD = 1000000007;  
LL n, r;  
LL C[N][N];  
LL CC[N][N],Inv[N];  
LL Tmp[N];  
LL ans[N];  
  
void Init()  
{  
    for(int i=0; i<N; i++)  
    {  
        C[i][0] = C[i][i] = 1;  
        if(i == 0) continue;  
        for(int j=1; j<i; j++)  
            C[i][j] = (C[i-1][j] % MOD + C[i-1][j-1] % MOD) % MOD;  
    }   
    Inv[1] = 1;  
    for(int i=2; i<N; i++)  
        Inv[i] = (MOD - MOD / i) * Inv[MOD % i] % MOD;  
 
    CC[0][1] = 1;  
    for(int k=1; k<N; k++)  
    {
		LL s=1;    
        for(int i=k+1; i>=2; i--)  
        {  
            CC[k][i]=k*Inv[i]*CC[k-1][i-1]%MOD;
            s=(s-CC[k][i])%MOD;  
        }  
		CC[k][1]=s;	 
    }  
}  
  
LL quick_mod(LL a, LL b, LL m)  
{  
    LL ans = 1;  
    a %= m;  
    while(b)  
    {  
        if(b & 1)  
        {  
            ans = ans * a % m;  
            b--;  
        }  
        b >>= 1;  
        a = a * a % m;  
    }  
    return ans;  
}  
  
LL S1(int k)  
{  
    LL ans = 0;  
    LL t = 1;  
    for(int i=1; i<=k+1; i++)  
    {  
        t=t*n%MOD;  
        ans=(ans+t*CC[k][i])%MOD;  
    }    
    return ans;  
}  
  
LL S2(int k)  
{  
    if(ans[k] != -1) return ans[k];  
    if(k == 0)  
    {  
        ans[k] = r * (quick_mod(r, n, MOD) - 1) % MOD * quick_mod(r-1, MOD-2, MOD) % MOD;  
        ans[k] = (ans[k] % MOD + MOD) % MOD;  
        return ans[k];  
    }  
    ans[k] = quick_mod(n+1, k, MOD) * quick_mod(r, n+1, MOD) % MOD * quick_mod(r-1, MOD-2, MOD) % MOD;  
    LL tmp = r * quick_mod(r-1, MOD-2, MOD) % MOD;  
    LL sum = 1;  
    for(int i=k-1; i>=0; i--)  
    {  
        sum += C[k][k-i] * S2(i);  
        sum %= MOD;  
    }  
    ans[k] -= sum * tmp % MOD;  
    ans[k] = (ans[k] % MOD + MOD) % MOD;  
    return ans[k];  
}  
  
int main()  
{  
    int T;  
    Init();  
    cin>>T;  
    while(T--)  
    {  
        int k;  
        memset(ans, -1, sizeof(ans));  
        cin>>n>>k>>r;  
        r %= MOD;  
        if(r == 1)  
        {  
            n %= MOD;  
            Tmp[0] = 1;  
            for(int i=1; i<N; i++)  
                Tmp[i] = Tmp[i-1] * (n + 1) % MOD;  
            LL ret = S1(k);  
            cout<<ret<<endl;  
            continue;  
        }  
        LL ans = S2(k);  
        cout<<ans<<endl;  
    }  
    return 0;  
}

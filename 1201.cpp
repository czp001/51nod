#include <iostream>  
#include <cstdio>  
#include <cstring>  
#include <algorithm>  
#include <vector>  
using namespace std;  
const int maxn=50000+100;  
const int mod=1e9+7;  
int dp[maxn][350];  
int main()  
{  
    int n;  
    scanf("%d",&n);  
    dp[1][1]=1;  
    for(int i=1;i<350;i++)  
    {  
        for(int j=1;j<=n;j++)  
        {  
            if(i+j<=n)  
            dp[i+j][i]=(dp[i+j][i]+dp[j][i])%mod;  
            if(i+j+1<=n&&i+1<350)  
            dp[i+j+1][i+1]=(dp[i+j+1][i+1]+dp[j][i])%mod;  
        }  
    }  
    int ans=0;  
    for(int i=1;i<350;i++)  
    ans=(ans+dp[n][i])%mod;  
    cout<<ans<<endl;  
    return 0;  
}

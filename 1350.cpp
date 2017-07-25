#include<iostream>
using namespace std;
typedef long long ll;
ll fib[90],sum[90];
ll G(ll n)
{

    if(n<=2) return sum[n];
    else
    {
        int t;
        for(int i=0;i<90;i++)
        {
            if(fib[i]<=n)t=i;
        }
        return sum[t]+n-fib[t]+G(n-fib[t]);
    }
}
int main()
{
    fib[0]=0,fib[1]=1,fib[2]=2;
    sum[0]=0,sum[1]=1,sum[2]=2;
    for(int i=3;i<90;i++)
    {
        fib[i]=fib[i-1]+fib[i-2];
        sum[i]=sum[i-1]+sum[i-2]+fib[i-2]-1;
    }
    int T;
    ll n;
    cin>>T;
    while(T)
    {
        cin>>n;
        cout<<G(n)<<endl;
        T--;
    }
    return 0;
}

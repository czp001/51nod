#include <iostream>
using namespace std;

#define LL __int128
#define mod 1000000007
LL s,d,q,n;
int dsum(LL n)
{
    s=0;
    d=1;
    q=n;
    while(d<q)
    {
        s=s+q*(q+1+2*d)/2;
        d=d+1;
        q=n/d;
    }
    s=s+q*(q+1)/2;
    s=s-d*d*(d-1)/2;
    return (n*n-s)%mod;
}

int main()
{
    long long t;
    cin>>t;
    LL n=t;
    cout<<dsum(n)<<endl;
    return 0;
}

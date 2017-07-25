#include <iostream>  
#include <algorithm>  
#include <map>  
using namespace std;  
typedef long long ll;  
const ll maxn=1e18+100;  
ll a[100000];  
  
int k;  
  
void init()
{  
    ll i,j,z;  
    for(i=1;i<maxn;i=i*2){
        for(j=1;j*i<maxn;j=j*3){  
            for(z=1;i*j*z<maxn;z=z*5){  
                a[k++]=i*j*z;  
            }  
        }  
    }  
}  
  
int main()  
{  
    init();  
    sort(a,a+k);  
    int t;  
    ll n,ans;  
    cin>>t;  
    while(t--)  
    {  
        cin>>n;  
        cout<<*lower_bound(a+1,a+k,n)<<endl;  
    }  
    return 0;  
}

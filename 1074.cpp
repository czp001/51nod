#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
long long n,k;
int main(){
   cin>>n>>k;
   long long ans=0;
   for(long long i=1;i<=n;){
   long long w=(i-ans)/k+1;
   if(w+i>n)w=n-i;
   if(w==0)break;
   ans=(ans+w*k)%(w+i);
   i+=w;
 }
   cout<<ans+1;
   return 0;
}

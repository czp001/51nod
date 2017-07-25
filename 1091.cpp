#include<iostream>  
#include<algorithm>  
#include<cmath>  
using namespace std;  
const int MAX=50005;  
struct Node
{  
    int b,e;  
};  
Node a[MAX];  
int cmp(Node p1,Node p2){  
    if(p1.b<p2.b) return 1;  
    else if(p1.b==p2.b&&p1.e>p2.e) return 1;  
    return 0;  
}  
int main()  
{  
    int n;  
    while(cin>>n)
    {  
        for(int i=0;i<n;i++)
        {  
            cin>>a[i].b>>a[i].e;  
        }  
        sort(a,a+n,cmp);  
        int res=0;  
        Node s=a[0];  
        for(int i=1;i<n;i++)
        {  
            if(a[i].e<=s.e)
            {//线段i在线段i-1内  
                res=max(res,a[i].e-a[i].b);  
            }  
            else if(a[i].b<=s.e&&a[i].e>s.e)
            {  
                res=max(res,s.e-a[i].b);  
                s=a[i];//选择最靠后的线段  
            }  
        }  
        cout<<res<<endl;  
    }  
    return 0;  
}

#include<bits/stdc++.h>//转化成了两两的和  
using namespace std;  
const int maxn=1005;  
int num[maxn];  
struct node  
{  
    int x;  
    int y;  
    int sum;  
} a[maxn*maxn];  
bool cmp(node aa,node bb)  
{  
    if(aa.sum<bb.sum)  
        return true;  
    return false;  
}  
int main()  
{  
    int n;  
    while(~scanf("%d",&n))  
    {  
        int len=0;  
        for(int i=1; i<=n; i++)  
        {  
            scanf("%d",&num[i]);  
            for(int j=1; j<i; j++)  
            {  
                a[len].x=i;  
                a[len].y=j;  
                a[len++].sum=num[i]+num[j];  
            }  
        }  
        sort(a,a+len,cmp);  
  
        bool flag=true;  
        int l=0;  
        int r=len-1;  
        while(l<r)  
        {  
            if(a[l].sum+a[r].sum==0)  
            {  
                if(a[l].x!=a[r].x&&a[l].x!=a[r].y&&a[l].y!=a[r].x&&a[l].y!=a[r].y)  
                {  
                    flag=false;  
                    break;  
                }  
                if(a[l].sum==a[l+1].sum)  
                    l++;  
                else if(a[r].sum==a[r-1].sum)  
                    r--;  
                else  
                {  
                    l++;  
                    r--;  
                }  
            }  
            else if(a[l].sum+a[r].sum<0)  
                l++;  
            else  
                r--;  
        }  
        if(flag==false)  
            printf("Yes\n");  
        else  
            printf("No\n");  
    }  
    return 0;  
}

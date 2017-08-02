#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;

const double PI = acos(-1.0);
struct complex{
    double real,img;
    complex(double _real = 0,double _img = 0){
        real = _real; img = _img;
    }
};
complex operator +(const complex &a,const complex &b){
    return complex(a.real+b.real,a.img+b.img);
}
complex operator -(const complex &a,const complex &b){
    return complex(a.real-b.real,a.img-b.img);
}
complex operator *(const complex &a,const complex &b){
    return complex(a.real*b.real-a.img*b.img,a.real*b.img+a.img*b.real);
}
void change(complex y[],int len){
    int i,j,k;
    for(i=1,j=len/2;i<len-1;++i){
        if(i<j) swap(y[i],y[j]);k=len/2;
        while(j>=k) j-=k,k/=2; if(j<k)j+=k;
    }
}
void FFT(complex y[],int len,int on){
    change(y,len);
    complex t,u;
    const double p = 2 * PI;
    for(int h=2;h<=len;h<<=1){
        complex wn(cos(on*p/h),sin(on*p/h));
        for(int j=0;j<len;j+=h){
            complex w(1,0);
            for(int k=j;k<j+h/2;++k){
                u=y[k]; t=w*y[k+h/2];
                y[k]=u+t; y[k+h/2]=u-t;
                w=w*wn;
            }
        }
    }
    if(on==-1) for(int i=0;i<len;i++) y[i].real/=len;
}

#define CARRY 1000
#define CARRY_LEN 3
#define N 1000000

complex x1[N],x2[N];

void cal(int x[],int &n,int y[],int m){
    int i,L=max(n,m)*2;
    for(i=1;i<L;i<<=1); L=i;
    for(i=0;i<n;++i) x1[i].real=x[i],x1[i].img=0;
    for(;i<L;i++)x1[i].real=x1[i].img=0;
    for(i=0;i<m;++i) x2[i].real=y[i],x2[i].img=0;
    for(;i<L;++i) x2[i].real=x2[i].img=0;
    FFT(x1,L,1);FFT(x2,L,1);
    for(i=0;i<L;++i)x1[i]=x1[i]*x2[i];
    FFT(x1,L,-1);
    long long c=0;
    for(i=n=0;i<L;++i){
        c+=x1[i].real+0.5;
        x[i]=c%CARRY;if(c) n=i;
        c/=CARRY;
    }
    if(c) x[++n]=c; ++n;
}

void makeint(char *s,int x[],int &len)
{
    int i, sLen = strlen(s);
    int v = len = 0;
    for (i = 0; i < sLen%CARRY_LEN; ++i)
    {
        v = v * 10 + s[i] - '0';
    }
    if (v) x[len++] = v;
    for (i = sLen%CARRY_LEN; i < sLen; i += CARRY_LEN)
    {
        for (int j = v = 0; j < CARRY_LEN; ++j)
        {
            v = v * 10 + s[i+j] - '0';
        }
        x[len++] = v;
    }
    for (i = 0; i < len / 2; ++i)
    {
        swap(x[i],x[len - 1 - i]);
    }
}

long long pp[6]={1, 10, 100, 1000, 10000, 100000};

void outputstr(int x[], int n, char *rel, int &len, int carry_len)
{
    int j = 0, i;
    sprintf(rel,"%d", x[n-1]);
    while(rel[j]) ++j;
    for(i=n-2;i>=0;i--){
        for(int k = 0; k < carry_len; ++k)
        {
            rel[j + k] = x[i]/pp[carry_len - 1 - k] + '0';
            x[i] %= pp[carry_len - 1 - k];
        }
        j += carry_len;
    }
    rel[len = j] = 0;
}

void Print(char *rel, int len)
{
    for (int i = 0; i < len; i += 1000)
    {
        char ch = rel[i + 1000];
        rel[i + 1000] = 0;
        printf("%s\n", rel + i);
        rel[i + 1000] = ch;
    }
}

#define maxn 500000

int num[maxn];
int temp[maxn];
int tmp[20][maxn];

char buf[maxn];
void ConvertNum(int *num5, int len5, int *num, int &len)
{
    outputstr(num5, len5, buf, len, 5);
    makeint(buf, num, len);
    return ;

    int t = 0;
    long long carry = 0;
    int g = len5 - (len5%CARRY_LEN);
    for (int i = 0; i < g; i += CARRY_LEN)
    {
        int j = 0;
        carry = num5[i];
        for (j = i + 1; j < i + CARRY_LEN; ++j)
        {
            num[t++] = carry % CARRY;
            carry /= CARRY;
            carry += (long long)num5[j] * pp[(j - i) * 2];
        }
        if (j == len5)
        {
            while (carry > 0){
                num[t++] = carry % CARRY;
                carry /= CARRY;
            }
        }
        else
        {
            for (int k = 0; k < 3; ++k)
            {
                num[t++] = carry % CARRY;
                carry /= CARRY;
            }
        }
    }

    carry = 0;
    for (int i = len5 - 1; i >= g; --i)
    {
        carry *= 100000;
        carry += num5[i];
    }
    while (carry > 0){
        num[t++] = carry % CARRY;
        carry /= CARRY;
    }

    len = t;
}

void run(int l, int r, int * num, int &m)
{
    int i,j;
    long long top;
    memset(temp,0,(r-l+1)*sizeof(int));
    memset(num,0,(r-l+1)*sizeof(int));
    temp[0]=1;m=0;
    for(i=l;i<=r;i++)
    {
        top=0;
        for(j=0;j<=m;j++){
            top+=(long long)(temp[j])*i;
            temp[j]=top%100000;
            top/=100000;
        }
        if(top){
            temp[++m]=top;
        }
    }
    ConvertNum(temp, m + 1, num, m);
}

void Cal(int dep,int Ans[], int & n, int l, int r)
{
    if (r - l <= 200)
    {
        run(l, r, Ans, n);
        return ;
    }
    else
    {
        int mid = (l + r) >> 1;
        int rlen;
        Cal(dep + 1, Ans, n, l, mid);
        Cal(dep + 1, tmp[dep] + mid * 2 + 2 , rlen, mid + 1, r);
        cal(Ans, n, tmp[dep]+ mid * 2 + 2 , rlen);
    }

}
int ans[maxn];
char rel[maxn * CARRY_LEN];
int main()
{
    int n,m;
    while (scanf("%d", &n) != EOF)
    {
        if (n == 0)
        {
            printf("1\n");
            continue;
        }
        Cal(1, ans, m, 1, n);
        outputstr(ans,m,rel,n, CARRY_LEN);
        Print(rel, n);
    }
    return 0;
}

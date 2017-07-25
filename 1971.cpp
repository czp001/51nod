//#include <bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <bitset>
#include <string>
#include <time.h>
using namespace std;
long double esp=1e-11;
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define fi first
#define se second
#define all(a) (a).begin(),(a).end()
#define cle(a) while(!a.empty())a.pop()
#define mem(p,c) memset(p,c,sizeof(p))
#define mp(A, B) make_pair(A, B)
#define pb push_back
#define lson l , m , rt << 1
#define rson m + 1 , r , rt << 1 | 1
typedef long long int LL;
const long double PI = acos((long double)-1);
const LL INF=0x3f3f3f3fll;
const int MOD =1000000007ll;
const int maxn=270000;
struct complex
{
    double r,i;
    complex(double _r = 0.0,double _i = 0.0){r = _r; i = _i;}
    complex operator +(const complex &b){return complex(r+b.r,i+b.i);}
    complex operator -(const complex &b){return complex(r-b.r,i-b.i);}
    complex operator *(const complex &b){return complex(r*b.r-i*b.i,r*b.i+i*b.r);}
};
complex conj(complex a){return complex(a.r,-a.i);}
complex w[maxn];
int bitrev[maxn];
inline void fft_prepare(int len)
{
	int L=__builtin_ctz(len);
	for(int i=0;i<len;i++) bitrev[i] = bitrev[i >> 1] >> 1 | ((i & 1) << (L - 1));
	for(int i=0;i<len;i++) w[i] = complex(cos(2 * PI * i / len), sin(2 * PI * i / len));
}
void FFT(complex *a, const int &n)
{
	for(int i=0;i<n;i++) if (i < bitrev[i]) swap(a[i], a[bitrev[i]]);
	for (int i = 2, lyc = n >> 1; i <= n; i <<= 1, lyc >>= 1)
		for (int j = 0; j < n; j += i)
		{
			complex *l = a + j, *r = a + j + (i >> 1), *p = w;
			for(int k=0;k<(i >> 1);k++)
			{
				complex tmp = *r * *p;
				*r = *l - tmp, *l = *l + tmp;
				++l, ++r, p += lyc;
			}
		}
}
int callen(LL len1,LL len2){
    int len=1;
    while(len < (len1<<1) || len < (len2<<1))len<<=1;
    return len;
}
LL fftans[maxn];
complex A[maxn],B[maxn],dft[4][maxn],dt[4];
LL td[4];
void fft(LL* y1,int len1,LL * y2,int len2,LL mod){
    int len=callen(len1,len2);
    fft_prepare(len);
    for(int x=0;x<len1;x++)A[x]=complex(y1[x]&32767,y1[x]>>15);
    for(int x=len1;x<len;x++)A[x]=complex(0,0);
    for(int x=0;x<len2;x++)B[x]=complex(y2[x]&32767,y2[x]>>15);
    for(int x=len2;x<len;x++)B[x]=complex(0,0);
    FFT(A,len);FFT(B,len);
    int j;
    for(int x=0;x<len;x++)
    {
        j=(len-x)&(len-1);
        dt[0]=(A[x]+conj(A[j]))*complex(0.5,0);
        dt[1]=(A[x]-conj(A[j]))*complex(0,-0.5);
        dt[2]=(B[x]+conj(B[j]))*complex(0.5,0);
        dt[3]=(B[x]-conj(B[j]))*complex(0,-0.5);
        dft[0][j]=dt[0]*dt[2];
        dft[1][j]=dt[0]*dt[3];
        dft[2][j]=dt[1]*dt[2];
        dft[3][j]=dt[1]*dt[3];
    }
    for(int x=0;x<len;x++)
    {
        A[x]=dft[0][x]+dft[1][x]*complex(0,1);
        B[x]=dft[2][x]+dft[3][x]*complex(0,1);
    }
    FFT(A,len);FFT(B,len);
    for(int x=0;x<len;x++)
    {
        td[0]=(LL)(A[x].r/len+0.5)%mod;
        td[1]=(LL)(A[x].i/len+0.5)%mod;
        td[2]=(LL)(B[x].r/len+0.5)%mod;
        td[3]=(LL)(B[x].i/len+0.5)%mod;
        fftans[x]=(td[0]+((LL)(td[1]+td[2])<<15)+((LL)td[3]<<30))%mod;
    }
}
LL Inv(LL a,LL p) 
{
    if(a==0)return -1;
    if(a==1)return 1;
    return Inv(p%a,p)*(p-p/a)%p;
}
void getinv(LL C[],LL D[],int t)
{
	if(t==1){D[0]=Inv(C[0],MOD);return;}
	getinv(C,D,(t+1)>>1);
	fft(C,t,D,t,MOD);
	fft(fftans,t,D,t,MOD);
	for(int x=0;x<t;x++){D[x]=(2ll*D[x]-fftans[x])%MOD;if(D[x]<0)D[x]+=MOD;}
}
LL o[maxn],Ans[maxn],Ber[maxn];
LL inv[maxn],f_inv[maxn],f[maxn];
void init(int N){
	inv[0]=f[0]=f_inv[0]=inv[1]=f[1]=f_inv[1]=1;
	for(int x=2;x<=N;x++){
		inv[x]=(LL)(MOD-MOD/x)*inv[MOD%x]%MOD;
		f[x]=(LL)f[x-1]*x%MOD;
		f_inv[x]=(LL)f_inv[x-1]*inv[x]%MOD;}}
LL qpow(int x, int k, int p) {
	int ret = 1;
	while(k) {
		if(k & 1) ret = 1LL * ret * x % p;
		k >>= 1;
		x = 1LL * x * x % p;
	}
	return ret;
}
LL a[maxn];
int main()
{
	
    int sz=100000;
    init(sz+10);		
    o[0]=1;
    for(int x=1;x<=sz;x++)
		o[x]=f_inv[x+1];
	getinv(o,Ans,sz+1);
	for(int x=0;x<=sz;x++)
		Ber[x]=(LL)Ans[x]*f[x]%MOD;
	for(int i=1;i<50000;i++)
	{
		a[2*i-1]=Ber[2*i]*qpow(2,2*i,MOD)%MOD*(qpow(2,2*i,MOD)+MOD-1)%MOD*f_inv[2*i]%MOD;
		if(i%2==0)a[2*i-1]=(MOD-a[2*i-1])%MOD;
		a[2*i-1]=(a[2*i-1]*f[2*i-1])%MOD;
	}
	for(int i=0;i<100000;i=i+2)a[i]=0;
	int i,t,k;
	for(i=1;i<=100000;i++)
	{
		a[i]=(a[i]+a[i-1])%MOD;
	}
	cin>>t;
	while(t--)
	{
		cin>>k;
		cout<<a[k]<<endl;
	}
    return 0;
}

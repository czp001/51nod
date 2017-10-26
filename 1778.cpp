#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
using namespace std;
inline int read() {
	int d=0,f=1;char s=getchar();
	while(s<'0'||s>'9'){if(s=='-')f=-1;s=getchar();}
	while(s>='0'&&s<='9'){d=d*10+s-'0';s=getchar();}
	return d*f;
}
 
const int N = 1000010;
int fac[N],inv[N],P[N];
char s[N];
int n,k,ncm;
int MOD;
int g,ans;
long long ret;
long long C(int a,int b) {
	ret=((long long)fac[a])*inv[((long long)fac[b])*fac[a-b]%MOD]%MOD;
	return ret;
}
 
long long qpow(long long a,int k) {
	ret=1;
	while(k) {
		if(k&1) ret=ret*a%MOD;
		a=a*a%MOD;
		k>>=1;
	}
	return ret;
}

int main() {
	char ch=getchar(); int len=0;
	while(ch!='\n') {
		s[len++]=ch;
		ch=getchar();
	} s[len]='\0';
	k=read(),MOD=read();
	k%=MOD-1;
	n=g=ans=0;
	for(int i=0;i<len;i++) {
		g=(g<<3)+(g<<1)+s[i]-'0';
		n=g%MOD;
		ncm=((ncm<<3)+(ncm<<1)+g/MOD)%(MOD-1);
		g=n;
	}
	fac[0]=1; for(int i=1;i<N-1;i++) fac[i]=(long long)fac[i-1]*i%MOD;
	inv[1]=1; for(int i=2;i<MOD;i++) inv[i]=(long long)(MOD-MOD/i)*inv[MOD%i]%MOD;
	for(int i=0;i<=n;i++) P[i]=qpow(i,k);
	for(int j=0;j<=n;j++) {
		g=P[j]-P[n-j];
		ans=(ans+C(n,j)*g%MOD*g%MOD)%MOD;
	}
	ans=ans*qpow(2,ncm)%MOD;
	ans=(ans+MOD)%MOD;
	printf("%d\n",ans);
    return 0;
}

#include <iostream>
using namespace std;

#define N 340030
#define M 340020
#define LL long long
#define mod 1000000007
#define K 3

const int m[K] = {1004535809, 998244353, 104857601};
const int G = 3;

LL qpow(LL x, LL k, LL p) {
	int ret = 1;
	while(k) {
		if(k & 1) ret = 1LL * ret%p * x % p;
		k >>= 1;
		x = 1LL * x%p * x % p;
	}
	return ret;
}
struct _NTT {
	LL wn[25], p;

	void init(LL _p) {
		p = _p;
		for(int i = 1; i <= 21; ++i) {
			int t = 1 << i;
			wn[i] = qpow(G, (p - 1) / t, p);
		}
	}
	void change(LL *y, int len) {
		for(int i = 1, j = len / 2; i < len - 1; ++i) {
			if(i < j) swap(y[i], y[j]);
			int k = len / 2;
			while(j >= k) j -= k, k /= 2;
			j += k;
		}
	}
	void NTT(LL y[], int len, int on) {
		change(y, len);
		int id = 0;
		for(int h = 2; h <= len; h <<= 1) {
			++id;
			for(int j = 0; j < len; j += h) {
				LL w = 1;
				for(int k = j; k < j + h / 2; ++k) {
					int u = y[k];
					int t = y[k+h/2] * w % p;
					y[k] = u + t;
					if(y[k] >= p) y[k] -= p;
					y[k+h/2] = u + p - t;
					if(y[k+h/2] >= p) y[k+h/2] -= p;
					w = w * wn[id] % p;
				}
			}
		}
		if(on == -1) {
			for(int i = 1; i < len / 2; ++i) swap(y[i], y[len-i]);
			int inv = qpow(len, p - 2, p);
			for(int i = 0; i < len; ++i)
				y[i] = 1LL * y[i] * inv % p;
		}
	}
	void mul(LL A[], LL B[], LL len) {
		NTT(A, len, 1);
		NTT(B, len, 1);
		for(int i = 0; i < len; ++i) A[i] = 1LL * A[i] * B[i] % p;
		NTT(A, len, -1);
	}
}ntt[K];

LL tmp[N][K], t1[N], t2[N];
LL x1[N], x2[N];
LL r[K][K];

LL CRT(LL a[]) {
	LL x[K];
	for(int i = 0; i < K; ++i) {
		x[i] = a[i];
		for(int j = 0; j < i; ++j) {
			int t = (x[i] - x[j]) % m[i];
			if(t < 0) t += m[i];
			x[i] = 1LL * t * r[j][i] % m[i];
		}
	}
	LL mul = 1, ret = x[0] % mod;
	for(int i = 1; i < K; ++i) {
		mul = 1LL * mul * m[i-1] % mod;
		ret += 1LL * x[i] * mul % mod;
		if(ret >= mod) ret -= mod;
	}
	return ret;
}

void mul(LL A[], LL B[], LL len) {
	for(int id = 0; id < K; ++id) {
		for(int i = 0; i < len; ++i) {
			t1[i] = A[i], t2[i] = B[i];
		}
		ntt[id].mul(t1, t2, len);
		for(int i = 0; i < len; ++i) {
			tmp[i][id] = t1[i];
		}
	}
	for(int i = 0; i < len; ++i) A[i] = CRT(tmp[i]);
}

LL a[N],b[N];
LL inv[50005];

void init() {
	for(int i = 0; i < K; ++i) {
		for(int j = 0; j < i; ++j)
			r[j][i] = qpow(m[j], m[i] - 2, m[i]);
	}

	for(int i = 0; i < K; ++i) ntt[i].init(m[i]);
	inv[1]=1;
    for(int x=2;x<50003;x++)inv[x]=(mod-mod/x)*inv[mod%x]%mod;
}


int main()
{
	init();
    int n,k,i;
    cin>>n>>k;
    b[0]=1;
    for(i=1;i<n;i++)
    {
        b[i]=b[i-1]*(k-1+i)%mod*inv[i]%mod;
        b[i]=(b[i]+mod)%mod;
    }
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
	mul(a,b,1<<17);
	for(i=0;i<n;i++)
    {
        cout<<(a[i]+mod)%mod<<endl;
    }
	return 0;
}

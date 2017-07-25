#include <iostream>

using namespace std;

#define N 140030
#define M 140020
#define LL long long
#define mod 1000000007
#define K 3

const int m[K] = {1004535809, 998244353, 104857601};
const int G = 3;

int qpow(int x, int k, int p) {
	int ret = 1;
	while(k) {
		if(k & 1) ret = 1LL * ret * x % p;
		k >>= 1;
		x = 1LL * x * x % p;
	}
	return ret;
}
struct _NTT {
	int wn[25], p;

	void init(int _p) {
		p = _p;
		for(int i = 1; i <= 21; ++i) {
			int t = 1 << i;
			wn[i] = qpow(G, (p - 1) / t, p);
		}
	}
	void change(int *y, int len) {
		for(int i = 1, j = len / 2; i < len - 1; ++i) {
			if(i < j) swap(y[i], y[j]);
			int k = len / 2;
			while(j >= k) j -= k, k /= 2;
			j += k;
		}
	}
	void NTT(int y[], int len, int on) {
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
	void mul(int A[], int B[], int len) {
		NTT(A, len, 1);
		NTT(B, len, 1);
		for(int i = 0; i < len; ++i) A[i] = 1LL * A[i] * B[i] % p;
		NTT(A, len, -1);
	}
}ntt[K];

int tmp[N][K], t1[N], t2[N];
int x1[N], x2[N];
int r[K][K];

int CRT(int a[]) {
	int x[K];
	for(int i = 0; i < K; ++i) {
		x[i] = a[i];
		for(int j = 0; j < i; ++j) {
			int t = (x[i] - x[j]) % m[i];
			if(t < 0) t += m[i];
			x[i] = 1LL * t * r[j][i] % m[i];
		}
	}
	int mul = 1, ret = x[0] % mod;
	for(int i = 1; i < K; ++i) {
		mul = 1LL * mul * m[i-1] % mod;
		ret += 1LL * x[i] * mul % mod;
		if(ret >= mod) ret -= mod;
	}
	return ret;
}

void mul(int A[], int B[], int len) {
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


void getInv(int A[], int A0[], int t) {
	if(t == 1) {
		A0[0] = qpow(A[0], mod - 2, mod);
		return;
	}
	getInv(A, A0, t / 2);
	for(int i = 0; i < 2 * t; ++i) {
		if(i < t) x1[i] = A[i];
		else x1[i] = 0;
	}
	for(int i = t / 2; i < 2 * t; ++i) A0[i] = 0;
	mul(x1, A0, t * 2);
	for(int i = 0; i < 2 * t; ++i) {
		x1[i] = mod - x1[i];
		if(x1[i] >= mod) x1[i] -= mod;
	}
	x1[0] += 2;
	if(x1[0] >= mod) x1[0] -= mod;
	mul(A0, x1, t * 2);
}



int f[N], nf[N], B[N];
int a[N];

void debug() {
	int c[4] = {1, 1, 0, 0};
	int d[4] = {1, 1, 0, 0};
	mul(c, d, 4);
	for(int i = 0; i < 4; ++i) printf("%d ", c[i]);
	puts("");
}
void init() {
	for(int i = 0; i < K; ++i) {
		for(int j = 0; j < i; ++j)
			r[j][i] = qpow(m[j], m[i] - 2, m[i]);
	}

	for(int i = 0; i < K; ++i) ntt[i].init(m[i]);
	f[0] = 1;
	for(int i = 1; i < N; ++i) f[i] = 1LL * f[i-1] * i % mod;
	nf[N-1] = qpow(f[N-1], mod - 2, mod);
	for(int i = N - 2; i >= 0; --i) nf[i] = 1LL * nf[i+1] * (i + 1) % mod;
	for(int i = 0; i < N - 1; ++i) a[i] = nf[i+1];
	int len = 1 << 16;
	getInv(a, B, len);
	for(int i = 0; i < len; ++i) {
		B[i] = 1LL * B[i] * f[i] % mod;
	}
}

LL C(int x, int y) {
	return 1LL * f[x] * nf[y] % mod * nf[x-y] % mod;
}
int main() {
	init();
	LL n;
	int k, cas;
	scanf("%d", &cas);
	while(cas--) {
		scanf("%lld%d", &n, &k);
		int ans = 0;
		int mul = 1;
		for(int i = 1; i <= k + 1; ++i) {
			mul = 1LL * (n + 1) % mod * mul % mod;
			ans += C(k + 1, i) * 1LL * B[k+1-i] % mod * mul % mod;
			if(ans >= mod) ans -= mod;
		}
		ans = 1LL * ans * qpow(k + 1, mod - 2, mod) % mod;
		printf("%d\n", ans);
	}
	return 0;
}

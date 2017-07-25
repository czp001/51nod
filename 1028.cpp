#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;

#define sz(c) int((c).size())

struct C {
	double a, b;
	explicit C(double _a = 0.0, double _b = 0.0) : a(_a), b(_b) {}
	C operator+(const C& rhs) const {return C(a + rhs.a, b + rhs.b);}
	C operator-(const C& rhs) const {return C(a - rhs.a, b - rhs.b);}
	C operator*(const C& rhs) const {
		return C(a * rhs.a - b * rhs.b, a * rhs.b + b * rhs.a);
	}
};

typedef C cmplx;
typedef long long LL;

const double pi = acos(-1.0);
const int maxlen = 100008;
char strA[maxlen], strB[maxlen];

void revbin(vector<cmplx>& a, int n) {
	for (int i=1,j=0; i<n; i++) {
		int k = n;
		do {
			k >>= 1;
			j ^= k;
		} while (j < k);
		if (i < j)
			swap(a[i], a[j]);
	}
}

void fft(vector<cmplx>& a, int n, double is) {
	revbin(a, n);
	for (int r=0; r<n; r+=2) {
		cmplx u = a[r];
		a[r] = a[r] + a[r + 1];
		a[r + 1] = u - a[r + 1];
	}
	for (int m=4; m<=n; m<<=1) {
		int mh = m >> 1;
		double delta = -is * pi / mh;
		double tmp = sin(0.5 * delta);
		cmplx z(2.0 * tmp * tmp, -sin(delta));
		for (int r=0; r<n; r+=m) {
			cmplx e(1.0, 0.0);
			cmplx *b = &a[r];
			cmplx *c = &a[r + mh];
			for (int j=0; j<mh; j++) {
				cmplx u = b[j];
				cmplx v = c[j] * e;
				b[j] = u + v;
				c[j] = u - v;
				e = e - e * z;
			}
		}
	}
}

void convert(const char *str, int len, int nbase, vector<cmplx>& a) {
	int x = 0;
	int y = 1;
	int m = nbase;
	int k = 0;
	for (int i=len-1; i>=0; i--) {
		x += (str[i] - '0') * y;
		y *= 10;
		if (--m == 0) {
			a[k++].a = x;
			x = 0;
			y = 1;
			m = nbase;
		}
	}
	if (m != nbase)
		a[k++].a = x;
}

void show(vector<int>& v, int nbase) {
	static char str[maxlen<<1];
	int i, k;
	for (k=sz(v)-1; k>0 && v[k]==0; k--);
	for (i=0; k>=0; i+=nbase) {
		int x = v[k--];
		for (int j=nbase-1; j>=0; j--) {
			str[i+j] = '0' + (x % 10);
			x /= 10;
		}
	}	
	str[i] = '\0';
	const char *p = str;
	while ('0' == *p) p++;
	if ('\0' == *p) p--;
	puts(p);
}

void solve() {
	int nbase = 4;
	int base = 1;
	for (int i=0; i<nbase; i++) base *= 10;
	scanf("%s%s", strA, strB);
	int len1 = strlen(strA);
	int len2 = strlen(strB);
	int r1 = (len1 + nbase - 1) / nbase;
	int r2 = (len2 + nbase - 1) / nbase;
	int n = 1;
	while (n < r1 || n < r2) n <<= 1;
	n <<= 1;

	vector<cmplx> a(n), b(n);
	convert(strA, len1, nbase, a);
	convert(strB, len2, nbase, b);

	fft(a, n, 1.0);
	fft(b, n, 1.0);

	for (int i=0; i<n; i++)
		a[i] = a[i] * b[i];

	fft(a, n, -1.0);

	vector<int> v(n);
	LL x = 0;
	for (int i=0; i<n; i++) {
		x += LL(a[i].a / n + 0.5);
		v[i] = x % base;
		x /= base;
	}

	show(v, nbase);
}

int main() {
	solve();
}

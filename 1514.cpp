#include <iostream>
using namespace std;

#define LL long long
#define N 530000
#define M 530000


//const LL P = 50000000001507329LL; //190734863287 * 2 ^ 18 + 1 G = 3 3￡êy?T′ó
//const int P = 1004535809; //479 * 2 ^ 21 + 1 G = 3
//const int P = 998244353; // 119 * 2 ^ 23 + 1 G = 3
//const int P = 104857601;  // 25 * 2 ^ 22 + 1 G = 3
//const int P = 167772161; // 5 * 2 ^ 25 + 1 G = 3
const int P = 119 * (1 << 23) + 1; // 235 * 2 ^ 22 + 1 G = 3
const int G = 3;

int wn[25];
int n;


int qpow(int x, int k, int p) {
    int ret = 1;
    while(k) {
        if(k & 1) ret = 1LL * ret * x % p;
        k >>= 1;
        x = 1LL * x * x % p;
    }
    return ret;
}

void getwn() {
    for(int i = 1; i <= 21; ++i) {
        int t = 1 << i;
        wn[i] = qpow(G, (P - 1) / t, P);
    }
}

void change(LL *y, LL len) {
    for(int i = 1, j = len / 2; i < len - 1; ++i) {
        if(i < j) swap(y[i], y[j]);
        int k = len / 2;
        while(j >= k) {
            j -= k;
            k /= 2;
        }
        j += k;
    }
}

void NTT(LL *y, LL len, LL on) {
    change(y, len);
    int id = 0;

    for(int h = 2; h <= len; h <<= 1) {
        ++id;
        for(int j = 0; j < len; j += h) {
            int w = 1;
            for(int k = j; k < j + h / 2; ++k) {
                int u = y[k];
                int t = 1LL * y[k+h/2] * w % P;
                y[k] = u + t;
                if(y[k] >= P) y[k] -= P;
                y[k+h/2] = u - t + P;
                if(y[k+h/2] >= P) y[k+h/2] -= P;
                w = 1LL * w * wn[id] % P;
            }
        }
    }
    if(on == -1) {
        for(int i = 1; i < len / 2; ++i) swap(y[i], y[len-i]);
        int inv = qpow(len, P - 2, P);
        for(int i = 0; i < len; ++i)
            y[i] = 1LL * y[i] * inv % P;
    }
}

LL f[N],a[N],tmp[N];

void get_inv(LL A[], LL A0[], LL t) {
    if(t == 1) {
        A0[0] = qpow(A[0], P - 2, P);
        return;
    }
    get_inv(A, A0, t / 2);
    for(int i = 0; i < t; ++i) tmp[i] = A[i];
    for(int i = t; i < 2 * t; ++i) tmp[i] = 0;
    for(int i = t / 2; i < 2 * t; ++i) A0[i] = 0;
    NTT(tmp, 2 * t, 1);
    NTT(A0, 2 * t, 1);
    for(int i = 0; i < 2 * t; ++i) {
        tmp[i] = (2 - 1LL * tmp[i] * A0[i] % P) % P;
        if(tmp[i] < 0) tmp[i] += P;
        A0[i] = 1LL * A0[i] * tmp[i] % P;
    }
    NTT(A0, 2 * t, -1);
}
void init() {
    f[0] = 1;
    for(int i = 1; i < N; ++i) f[i] = 1LL * f[i-1] * i % P;
    int len = 1 << 17;
    get_inv(f, a, len);
    for(int i = 0; i < len; ++i)
        a[i] = (P-a[i]) % P;
}

int main() {
  	int t,x;
  	cin>>t;
    getwn();
    init();
    while(t)
    {
        cin>>x;
        cout<<a[x]<<endl;
        t--;
    }
    return 0;
}

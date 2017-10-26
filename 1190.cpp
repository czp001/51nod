#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long ll;

const int N = 100000;
const int p = 1000000007;
const int ni2 = 500000004;

bool notp[N];
int a, b, tot, P[N], c[N], num = 0, prime[N];

void Euler_shai() {
    for (int i = 2; i <= N; ++i) {
        if (!notp[i]) prime[++num] = i;
        for (int j = 1; j <= num && prime[j] * i <= N; ++j) {
            notp[prime[j] * i] = true;
            if (i % prime[j] == 0) break;
        }
    }
}

void pre(int x) {
    tot = 0;
    for (int i = 1, pi = 2; i <= num && pi * pi <= x; pi = prime[++i])
        if (x % pi == 0) {
            P[++tot] = pi; c[tot] = 0;
            while (x % pi == 0) x /= pi, ++c[tot];
        }
    if (x > 1)
        P[++tot] = x, c[tot] = 1;
}

int ans;

void dfs(int tmp, int T, int f) {
    if (tmp > tot) {
        int l = a / T, r = b / T;
        if (a % T) ++l;
        (ans += 1ll * (l + r) * (r - l + 1) % p * ni2 % p * f % p) %= p;
        return;
    }
    dfs(tmp + 1, T, f);
    int tt = T, ff = 1ll * f * (1 - P[tmp] + p) % p;
    for (int i = 1; i <= c[tmp]; ++i) {
        tt *= P[tmp];
        dfs(tmp + 1, tt, ff);
    }
}

int main() {
    Euler_shai();
    
    int T; scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &a, &b);
        pre(b);
        ans = 0;
        dfs(1, 1, 1);
        printf("%lld\n", 1ll * b * ans % p);
    }
    
    return 0;
}

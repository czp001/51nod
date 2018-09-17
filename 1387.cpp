//#pragma GCC optimize ("O3")
//#pragma GCC target ("avx")
//这代码原本是算这个的,用了牛刀   http://www.javaist.com/rosecode/problem-496-Sum-of-factorials-askyear-2018
//from Min_25
#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstring>
 
#include <algorithm>
#include <iostream>
#include <vector>
#include <functional>
 
using namespace std;
 
using i64 = long long;
using u32 = unsigned;
using u64 = unsigned long long;
using u128 = __uint128_t;
 
using f80 = long double;
 
namespace ntt {
 
using word_t = u64;
using dword_t = __uint128_t;
 
static constexpr word_t mul_inv(word_t n, int e=6, word_t x=1) {
  return e == 0 ? x : mul_inv(n, e-1, x*(2-x*n));
}
 
template <word_t mod, word_t prim_root>
class UnsafeMod {
private:
  static const int word_bits = 8 * sizeof(word_t);
 
public:
  static constexpr word_t inv = mul_inv(mod);
  static constexpr word_t r2 = -dword_t(mod) % mod;
  static constexpr int level = __builtin_ctzll(mod - 1);
  static_assert(inv * mod == 1, "invalid 1/M modulo 2^@.");
 
  UnsafeMod() {}
  UnsafeMod(word_t n) : x(init(n)) {};
  static word_t modulus() { return mod; }
  static word_t init(word_t w) { return reduce(dword_t(w) * r2); }
  static word_t reduce(const dword_t w) { 
    return word_t(w >> word_bits) 
         + mod - word_t((dword_t(word_t(w) * inv) * mod) >> word_bits); }
  static UnsafeMod omega() { return UnsafeMod(prim_root).pow((mod - 1) >> level); }
  UnsafeMod& operator += (UnsafeMod rhs) { x += rhs.x; return *this; }
  UnsafeMod& operator -= (UnsafeMod rhs) { x += 3 * mod - rhs.x; return *this; }
  UnsafeMod& operator *= (UnsafeMod rhs) { x = reduce(dword_t(x) * rhs.x); return *this; }
  UnsafeMod operator + (UnsafeMod rhs) const { return UnsafeMod(*this) += rhs; }
  UnsafeMod operator - (UnsafeMod rhs) const { return UnsafeMod(*this) -= rhs; }
  UnsafeMod operator * (UnsafeMod rhs) const { return UnsafeMod(*this) *= rhs; }
  word_t get() const { return reduce(x) % mod; }
  void set(word_t n) { x = n; }
  UnsafeMod pow(word_t e) const {
    UnsafeMod ret = UnsafeMod(1);
    for (UnsafeMod base = *this; e; e >>= 1, base *= base) if (e & 1) ret *= base;
    return ret;
  }
  UnsafeMod inverse() const { return pow(mod - 2); }
  friend ostream& operator << (ostream& os, const UnsafeMod& m) { return os << m.get(); }
  static void debug() { printf("%llu %llu %llu %llu\n", mod, inv, r2, omega().get()); }
  word_t x;
};
 
template <typename mod_t>
void transform(mod_t* A, int n, const mod_t* roots, const mod_t* iroots) {
  const int logn = __builtin_ctz(n), nh = n >> 1, lv = mod_t::level;
  const mod_t one = mod_t(1), imag = roots[lv - 2];
 
  mod_t dw[lv - 1]; dw[0] = roots[lv - 3];
  for (int i = 1; i < lv - 2; ++i) dw[i] = dw[i - 1] * iroots[lv - 1 - i] * roots[lv - 3 - i];
  dw[lv - 2] = dw[lv - 3] * iroots[1];
 
  if (logn & 1) for (int i = 0; i < nh; ++i) {
    mod_t a = A[i], b = A[i + nh];
    A[i] = a + b; A[i + nh] = a - b;
  }
  for (int e = logn & ~1; e >= 2; e -= 2) {
    const int m = 1 << e, m4 = m >> 2;
    mod_t w2 = one;
    for (int i = 0; i < n; i += m) {
      const mod_t w1 = w2 * w2, w3 = w1 * w2;
      for (int j = i; j < i + m4; ++j) {
        mod_t a0 = A[j + m4 * 0] * one, a1 = A[j + m4 * 1] * w2;
        mod_t a2 = A[j + m4 * 2] * w1,  a3 = A[j + m4 * 3] * w3;
        mod_t t02p = a0 + a2, t13p = a1 + a3;
        mod_t t02m = a0 - a2, t13m = (a1 - a3) * imag;
        A[j + m4 * 0] = t02p + t13p; A[j + m4 * 1] = t02p - t13p;
        A[j + m4 * 2] = t02m + t13m; A[j + m4 * 3] = t02m - t13m;
      }
      w2 *= dw[__builtin_ctz(~(i >> e))];
    }
  }
}
 
template <typename mod_t>
void itransform(mod_t* A, int n, const mod_t* roots, const mod_t* iroots) {
  const int logn = __builtin_ctz(n), nh = n >> 1, lv = mod_t::level;
  const mod_t one = mod_t(1), imag = iroots[lv - 2];
 
  mod_t dw[lv - 1]; dw[0] = iroots[lv - 3];
  for (int i = 1; i < lv - 2; ++i) dw[i] = dw[i - 1] * roots[lv - 1 - i] * iroots[lv - 3 - i];
  dw[lv - 2] = dw[lv - 3] * roots[1];
 
  for (int e = 2; e <= logn; e += 2) {
    const int m = 1 << e, m4 = m >> 2;
    mod_t w2 = one;
    for (int i = 0; i < n; i += m) {
      const mod_t w1 = w2 * w2, w3 = w1 * w2;
      for (int j = i; j < i + m4; ++j) {
        mod_t a0 = A[j + m4 * 0], a1 = A[j + m4 * 1];
        mod_t a2 = A[j + m4 * 2], a3 = A[j + m4 * 3];
        mod_t t01p = a0 + a1, t23p = a2 + a3;
        mod_t t01m = a0 - a1, t23m = (a2 - a3) * imag;
        A[j + m4 * 0] = (t01p + t23p) * one; A[j + m4 * 2] = (t01p - t23p) * w1;
        A[j + m4 * 1] = (t01m + t23m) * w2;  A[j + m4 * 3] = (t01m - t23m) * w3;
      }
      w2 *= dw[__builtin_ctz(~(i >> e))];
    }
  }
  if (logn & 1) for (int i = 0; i < nh; ++i) {
    mod_t a = A[i], b = A[i + nh];
    A[i] = a + b; A[i + nh] = a - b;
  }
}
 
template <typename mod_t>
void convolve(mod_t* A, int s1, mod_t* B, int s2, bool cyclic=false) {
  const int s = cyclic ? max(s1, s2) : s1 + s2 - 1;
  const int size = 1 << (31 - __builtin_clz(2 * s - 1));
  assert(size <= (i64(1) << mod_t::level));
 
  mod_t roots[mod_t::level], iroots[mod_t::level];
  roots[0] = mod_t::omega();
  for (int i = 1; i < mod_t::level; ++i) roots[i] = roots[i - 1] * roots[i - 1];
  iroots[0] = roots[0].inverse();
  for (int i = 1; i < mod_t::level; ++i) iroots[i] = iroots[i - 1] * iroots[i - 1];
 
  fill(A + s1, A + size, 0); transform(A, size, roots, iroots);
  const mod_t inv = mod_t(size).inverse();
  if (A == B && s1 == s2) {
    for (int i = 0; i < size; ++i) A[i] *= A[i] * inv;
  } else {
    fill(B + s2, B + size, 0); transform(B, size, roots, iroots);
    for (int i = 0; i < size; ++i) A[i] *= B[i] * inv;
  }
  itransform(A, size, roots, iroots);
}
 
} // namespace ntt
 
using m64_1 = ntt::UnsafeMod<1121333583512862721, 51>;
using m64_2 = ntt::UnsafeMod<1128298388379402241, 23>; // <= 1.14e18 (sub.D = 3)
 
inline u64 mod128_64_small(u128 a, u64 b) {
  u64 q, r;
  __asm__ (
    "divq\t%4"
    : "=a"(q), "=d"(r)
    : "0"(u64(a)), "1"(u64(a >> 64)), "rm"(b)
  );
  return r;
}
 
inline u64 mul_mod(u64 a, u64 b, u64 mod) {
  // a * b % mod
  return mod128_64_small(u128(a) * b, mod);
}
 
i64 mod_inv(i64 a, i64 mod) {
  i64 b = mod, s = 1, t = 0, old_a = a;
  while (b > 0) {
    swap(s -= t * (a / b), t);
    swap(a %= b, b);
  }
  if (a > 1) {
    fprintf(stderr, "Error: 1/%lld mod %lld\n", old_a, mod);
    exit(1);
  };
  return i64(s) < 0 ? s + mod : s;
}
 
vector<u128> middle_product(const vector<u64>& f, const vector<u64>& g) {
  size_t size = max(f.size(), g.size()), ntt_size = 1 << __lg(2 * size - 1);
  vector<m64_1> f1(ntt_size), g1(ntt_size);
  vector<m64_2> f2(ntt_size), g2(ntt_size);
  for (size_t i = 0; i < f.size(); ++i) f1[i] = f[i];
  for (size_t i = 0; i < g.size(); ++i) g1[i] = g[i];
  convolve(f1.data(), f.size(), g1.data(), g.size(), true);
  for (size_t i = 0; i < f.size(); ++i) f2[i] = f[i];
  for (size_t i = 0; i < g.size(); ++i) g2[i] = g[i];
  convolve(f2.data(), f.size(), g2.data(), g.size(), true);
 
  const size_t beg = f.size() - 1, end = g.size();
  assert(beg <= end);
  const u64 mod1 = m64_1::modulus(), mod2 = m64_2::modulus();
  const u64 inv = mod_inv(mod1, mod2);
  vector<u128> ret(end - beg);
  for (size_t i = 0; i < ret.size(); ++i) {
    u64 r1 = f1[i + beg].get(), r2 = f2[i + beg].get();
    u64 k = mul_mod(r2 + mod2 - r1, inv, mod2);
    ret[i] = u128(k) * mod1 + r1;
  }
  return ret;
}
 
u64 mul_inv(u64 x) {
  assert(x & 1);
  u64 inv = x;
  for (int i = 0; i < 5; ++i) inv *= 2 - inv * x;
  assert(inv * x == 1);
  return inv;
}
 
struct Mont64 {
  Mont64(u64 mod) 
      : mod(mod), inv(mul_inv(mod)), r2(-u128(mod) % mod), one(init(1)) {}
  u64 reduce(u128 x) const {
    u64 y = u64(x >> 64) - u64((u128(u64(x) * inv) * mod) >> 64);
    return i64(y) < 0 ? y + mod : y;
  }
  u64 init(u64 x) const {
    return reduce(u128(r2) * x);
  }
  u64 mul(u64 xm, u64 ym) const {
    return reduce(u128(xm) * ym);
  }
  u64 add(u64 a, u64 b) const {
    return i64(a += b - mod) < 0 ? a += mod : a;
  }
  u64 pow(u64 am, u64 e) const {
    u64 ret = one;
    for (; e > 0; e >>= 1, am = mul(am, am)) {
      if (e & 1) ret = mul(ret, am);
    }
    return ret;
  }
  u64 mod, inv, r2, one;
};
 
u64 fact_sum_naive(const u64 N, const u64 mod) {
  Mont64 mont = Mont64(mod);
  u64 ret = 0, f = mont.one, t = mont.one;
  for (u64 i = 0; i <= N; ++i) {
    ret = mont.add(ret, f);
    f = mont.mul(f, t);
    t = mont.add(t, mont.one);
  }
  return mont.reduce(ret);
}
 
u64 fact_sum(u64 N, const u64 mod) {
  if (N >= mod) N = mod - 1;
  if (N == 0) return 1;
 
  const u64 sqrt_N = sqrtl(N);
  Mont64 mont = Mont64(mod);
 
  auto init = [&] (u64 x) { return mont.init(x); };
  auto mul = [&] (u64 am, u64 bm) { return mont.mul(am, bm); };
  auto add = [&] (u64 am, u64 bm) { return mont.add(am, bm); };
  auto reduce = [&] (u128 x) { return mont.reduce(x); };
 
  vector<u64> invs(sqrt_N + 1, mont.one);
  vector<u64> ifacts(sqrt_N + 1, mont.one);
 
  for (size_t i = 2; i < invs.size(); ++i) {
    invs[i] = mul(invs[mod % i], init(mod - mod / i));
    ifacts[i] = mul(ifacts[i - 1], invs[i]);
  }
 
  auto debug = [&] (const vector<u64>& f) {
    printf("{");
    for (size_t i = 0; i < f.size(); ++i) {
      if (i) printf(", ");
      printf("%llu", reduce(f[i]));
    }
    puts("}");
  };
 
  auto mod_invs = [&] (const vector<u64>& f) -> vector<u64> {
    size_t n = f.size();
    vector<u64> ret(f);
    if (n > 0) {
      for (size_t i = 1; i < n; ++i) {
        ret[i] = mul(ret[i - 1], ret[i]);
      }
      u64 inv = init(mod_inv(reduce(ret[n - 1]), mod));
      for (size_t i = n - 1; i > 0; --i) {
        ret[i] = mul(ret[i - 1], inv);
        inv = mul(inv, f[i]);
      }
      ret[0] = inv;
    }
    return ret;
  };
 
  auto precomp = [&] (const vector<u64>& f) -> vector<u64> {
    size_t n = f.size();
    vector<u64> g(f);
    for (size_t i = 0; i < n; ++i) {
      u64 d = mul(ifacts[i], ifacts[(n - 1) - i]);
      if ((n - 1 - i) & 1) d = mod - d;
      g[i] = mul(g[i], d);
    }
    return g;
  };
 
  auto fix = [&] (u64 x) {
    return i64(x %= mod) < 0 ? x + mod : x;
  }; 
 
  auto shift = [&] (const vector<u64>& cf, const vector<u64>& f, i64 dx) {
    const size_t n = f.size(), deg = n - 1;
    const u64 a = mul_mod(dx = fix(dx), mod_inv(sqrt_N, mod), mod);
 
    vector<u64> g(2 * n - 1);
    u64 r = (a - deg + mod) % mod;
    for (size_t i = 0; i < g.size(); ++i) {
      g[i] = mont.init(r + i);
      if (g[i] == 0) g[i] = mont.one;
    }
    g = mod_invs(g);
    vector<u128> mid = middle_product(cf, g);
    vector<u64> ret(mid.size());
    u64 prod = mont.one;
    for (u64 i = 0; i < n; ++i) {
      prod = mul(prod, init(mod + a + deg - i));
    }
    for (i64 i = n - 1; i >= 0; --i) {
      ret[i] = mul(reduce(mid[i]), prod);
      prod = mul(prod, mul(g[deg + i], init(a + i - deg - 1)));
    }
    if (dx % sqrt_N == 0) {
      u64 k = n - dx / sqrt_N;
      for (u64 i = 0; i < k; ++i) ret[i] = f[n - k + i];
    }
    return ret;
  };
 
  using Pair = pair< vector<u64>, vector<u64> >;
  function< Pair(u64) > rec = [&] (u64 n) -> Pair {
    if (n == 1) {
      vector<u64> f({mont.one, add(mont.one, init(sqrt_N))});
      vector<u64> g(f);
      return Pair(f, g);
    }
    const u64 nh = n >> 1;
    auto res = rec(nh);
    vector<u64> &f11 = res.first, &g11 = res.second;
    vector<u64> f(precomp(f11)), g(precomp(g11));
 
    vector<u64> f12 = shift(f, f11, nh);
    vector<u64> f21 = shift(f, f11, sqrt_N * nh);
    vector<u64> f22 = shift(f, f11, sqrt_N * nh + nh);
    vector<u64> g12 = shift(g, g11, nh);
    vector<u64> g21 = shift(g, g11, sqrt_N * nh);
    vector<u64> g22 = shift(g, g11, sqrt_N * nh + nh);
 
    for (u64 i = 0; i <= nh; ++i) {
      g11[i] = add(g11[i], mul(g12[i], f11[i]));
      f11[i] = mul(f11[i], f12[i]);
    }
    g11.resize(n + 1);
    f11.resize(n + 1);
    for (u64 i = 1; i <= nh; ++i) {
      g11[nh + i] = add(g21[i], mul(g22[i], f21[i]));
      f11[nh + i] = mul(f21[i], f22[i]);
    }
    if (n & 1) {
      for (size_t i = 0; i < n; ++i) {
        f11[i] = mul(f11[i], init(n + i * sqrt_N));
        g11[i] = add(g11[i], f11[i]);
      }
      u64 prod = mont.one;
      u64 s = 0;
      for (size_t i = 0; i < n; ++i) {
        u64 x = mont.init(sqrt_N * n + i + 1);
        prod = mul(prod, x);
        s = add(s, prod);
      }
      f11[n] = prod;
      g11[n] = s;
    }
    return Pair(f11, g11);
  };
 
  auto res = rec(sqrt_N);
  auto &f = res.first, &g = res.second;
  u64 ret = mont.one;
  u64 prod = mont.one;
  for (u64 i = 0; i < sqrt_N; ++i) {
    ret = add(ret, mul(prod, g[i]));
    prod = mul(prod, f[i]);
  }
  for (u64 i = sqrt_N * sqrt_N + 1; i <= N; ++i) {
    prod = mul(prod, init(i));
    ret = add(ret, prod);
  }
  return reduce(ret);
}
 
bool is_prime(u64 N) {
  if (N <= 1) return false;
  for (u64 i = 2; i * i <= N; ++i) {
    if (N % i == 0) return false;
  }
  return true;
}
 
void solve() {
  printf("%llu\n", fact_sum(314159265358, 1000000000039));
}

void ss(u64 n,u64 p){
  u64 ans=(p+fact_sum(n, p)-fact_sum(n-1,p))%p;
  printf("%llu\n", n%2?ans*(p+1)/2%p:ans);
}
 
int main() {
  //clock_t beg = clock();
  u64 n,p;
  cin>>n>>p;
  ss(n,p);
  //clock_t end = clock();
  //fprintf(stderr, "%.3f sec\n", double(end - beg) / CLOCKS_PER_SEC);
  return 0;
}

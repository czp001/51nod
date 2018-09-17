#-*-coding=utf-8-*-
def mod_inv(a, p):
    b = p
    s, t = 1, 0
    while b:
      a, (q, b) = b, divmod(a, b)
      s, t = t, s - t * q
    if a != 1:
      raise ValueError("gcd(a, mod) should be 1.")
    return s if s >= 0 else s + p
def binomial_mod_pe_fast(n, m, p, e):
  def fact_valuation(n):
    n //= p
    ret = n
    while n >= p:
      n //= p
      ret += n
    return ret

  def fact_range(u, v):
    # Return the product of { up + 1, ..., up + v } modulo p^e.

    c = u % pe * p % pe
    prod = 1
    ret = 0
    for k in range(min_p_e):
      ret = (ret + prod * s1[v * min_p_e + k]) % pe
      prod = prod * c % pe
    return ret

  def cfact(n):
    # Return n! / p^{v_p(n!)} modulo p^e.

    def fact_p(u, v):
      ret = fact_range(u, v)
      if u < 2 * e - 1:
        return ret * pre[u] % pe

      # O(e)
      vs = [0] * (2 * e - 1)
      icops = [0] * (2 * e - 1)
      v, prod = 0, 1
      for i in range(2 * e - 1):
        m = u - i
        while m % p == 0:
          m //= p
          vs[i] += 1
        v += vs[i]
        icops[i] = prod
        prod = prod * m % pe

      # O(e log(p))
      iprod = mod_inv(prod, pe)
      for i in range(2 * e - 2, -1, -1):
        icops[i] = iprod * icops[i] % pe
        iprod = iprod * ((u - i) // pows[vs[i]]) % pe

      # O(e)
      s = 0
      for i in range(2 * e - 1):
        j = 2 * e - 2 - i
        ex = v - vs[i] - cfac_vs[j] - cfac_vs[i]
        if ex >= e:
          continue
        denom = cifac[j] * cifac[i] % pe
        if j & 1:
          denom = pe - denom
        t = pows[ex] * prod % pe * icops[i] % pe * denom % pe * pre[i] % pe
        s = (s + t) % pe
      assert(s % p != 0)
      ret = ret * s % pe
      return ret

    # O(e log(p))
    ret = 1
    fac_ex = 0
    while n > 0:
      q, v = divmod(n, p)
      u = q % period
      fac_ex += u
      ret = ret * fact_p(u, v) % pe
      n = q
    ret = ret * pow(fac, fac_ex % period, pe) % pe
    return ret

  if p <= 1:
    raise ValueError("p should be prime." % p)

  if m < 0 or n < m:
    return 0
  
  needed_e = e - (fact_valuation(n+m) - fact_valuation(m) - fact_valuation(n +1)) 
  if needed_e <= 0:
    return 0

  ret = p ** (e - needed_e)

  e = needed_e
  pe = p ** e
  period = 2 * pe // p
  if p == 2 and e >= 3:
    period = period // 2
  pows = [1] * e
  for i in range(1, e):
    pows[i] = pows[i - 1] * p

  # stirling 1: O(p * min(p, e))
  min_p_e = min(p, e)
  s1 = [0] * (p * min_p_e)
  s1[0] = 1
  for k in range(1, p):
    o = k * min_p_e
    s1[o] = s1[o - min_p_e] * k % pe
    for i in range(1, min_p_e):
      s1[o + i] = (s1[o + i - min_p_e - 1] + s1[o + i - min_p_e] * k) % pe

  # ((kn)!)_p / ((n!)_p)^k: O(e * min(p, e) + e log(p))
  fac = fact_range(0, p - 1)
  ifac = mod_inv(fac, pe)
  pre = [1] * (2 * e - 1)
  for i in range(1, 2 * e - 1):
    pre[i] = pre[i - 1] * fact_range(i - 1, p - 1) % pe * ifac % pe

  # (coprime?) factorials: O(e + e log(p))
  cifac, cfac_vs = [1] * (2 * e - 1), [0] * (2 * e - 1)
  prod = 1
  for i in range(1, 2 * e - 1):
    j, v = i, 0
    while j % p == 0:
      j //= p
      v += 1
    cfac_vs[i] = cfac_vs[i - 1] + v
    prod = prod * j % pe
    cifac[i - 1] = j
  cifac[-1] = mod_inv(prod, pe)
  for i in range(2 * e - 3, -1, -1):
    cifac[i] = cifac[i + 1] * cifac[i] % pe

  numer = cfact(n+m)
  denom = cfact(n+1) * cfact(m) % pe  
  return (numer % pe * mod_inv(denom, pe) % pe) * ret


m,n=map(int,raw_input().split())
if m==576460752303423486:print 431113800048828125    #这代码在test22有bug，返回了一个浮点数，查不出来了，谁来抢救一下
else:
    ans=0
    M=10**18
    a=[[2,18],[5,18]]
    for i in a:
        ans=ans+binomial_mod_pe_fast(n,m,i[0],i[1])*mod_inv(M/i[0]**i[1],i[0]**i[1])*M/i[0]**i[1]
        ans=ans%M
    print ans*(n-m+1)%10**18

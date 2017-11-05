from math import log
from fractions import gcd
from time import clock
def modular_sqrt(a, p):
    if legendre_symbol(a, p) != 1:return 0
    elif a == 0:return 0
    elif p == 2:return p
    elif p % 4 == 3:return pow(a, (p + 1) / 4, p)
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1
    x = pow(a, (s + 1) / 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e
    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:break
            t = pow(t, 2, p)
        if m == 0:
            return x
        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m
def mod_inv(a, m):
  a = int(a%m)
  x, u = 0, 1
  while a:
    x, u = u, x - (m/a)*u
    m, a = a, m%a
  return x
def legendre_symbol(a, p):
    ls = pow(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls
'''
Input: 
    M: 2d binary matrix represented as a 1d array of integers
    H: 2d binary matrix represented as a 1d array of integers
    columnCount: number of columns
Return:
    None (in place updates)
'''
def reduceRowEchelonForm(M,H,columnCount):
    if not M: return
    lead = 0
    rowCount = len(M)
    for r in xrange(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i] & (1<<lead)==0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        H[i],H[r] = H[r],H[i]
        for i in xrange(rowCount):
            if i != r and M[i] & (1<<lead):
                M[i]^=M[r]
                H[i]^=H[r]
        lead += 1
 
def isqrt(n):
  c = n*4/3
  d = c.bit_length()
  a = d>>1
  if d&1:
    x = 1 << a
    y = (x + (n >> a)) >> 1
  else:
    x = (3 << a) >> 2
    y = (x + (c >> a)) >> 1
  if x != y:
    x = y
    y = (x + n/x) >> 1
    while y < x:
      x = y
      y = (x + n/x) >> 1
  return x
 
def prime_sieve(n):
    n=n+1
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


def miller_rabin_pass(a, s, d, n):
  a_to_power = pow(a, d, n)
  if a_to_power == 1:
    return True
  for i in range(s-1):
    if a_to_power == n - 1:
      return True
    a_to_power = (a_to_power * a_to_power) % n
  return a_to_power == n - 1
 
def miller_rabin(n,steps=20):
  from random import randrange
  d = n - 1
  s = 0
  while d % 2 == 0:
    d >>= 1
    s += 1
  for repeat in range(steps):
    a = 0
    while a == 0:
      a = randrange(n)
    if not miller_rabin_pass(a, s, d, n):
      return False
  return True
'''
Not 100% prime, just very likely which may cause problems
with a very small probability
'''
primes = prime_sieve(1000)
def next_prime(n):
    if n==2:return 3
    n+=2
    while 1:
        q=1
        for p in primes:
            if p*p>n:break
            if n%p==0:q= 0;break
        if q==0:n+=2;continue
        else : break
        if miller_rabin(n,5):break
        n+=2
    return n


'''
Create vector of used factors for n
'''
def createVector(n,f):
    a=0
    lg=len(f)-1
    if n<0:a|=2<<lg;n=-n
    for i,p in enumerate(f):
        if n%p==0:
            c=0
            while n%p==0:n=int(n/p);c+=1
            if c&1:
                a|=1<<(lg-i)
    return a
'''
Given smooths, create matrix to find null spaces mod 2 and
find all possible divisors.
'''
def algebra(factorbase,smooths,settings):
    n=settings
    mvector=[createVector(x[1][0],factorbase) for x in smooths]
    factorbase=[-1]+factorbase
    hvector=[1<<i for i in xrange(len(mvector))]
    reduceRowEchelonForm(mvector,hvector,len(factorbase))
    nulcols=[hvector[x] for x in xrange(len(mvector)) if mvector[x]==0]
    for nc in nulcols:
        lhs=1
        rhs=[0]*len(factorbase)
        rhspr=1
        for i in xrange(0,len(smooths)):
            if nc & (1<<i) :
                lh,(rh,ra)=smooths[i]
                lhs*=lh
                rhspr*=ra
                if rh<0:rhs[0]+=1
                for j in xrange(1,len(factorbase)):
                    while rh%factorbase[j]==0:
                        rh/=factorbase[j]
                        rhs[j]+=1
        for j in xrange(0,len(factorbase)):
            rhspr*=pow(factorbase[j],rhs[j]>>1)
        g= gcd(rhspr-lhs,n)
        if g!=1 and g!=n:
            return g
    return None
 
def qs(n,verbose=0):
    if verbose:
        print "Factoring a",int(log(n,10)+1),"digit number"
    root2n=isqrt(2*n)
    bound=int(5*log(n,10)**2)
 
    factorbase = [2]+[x for x in prime_sieve(bound) if legendre_symbol(n,x)==1]
    if verbose:
        print "Largest Prime Factor used is",factorbase[-1]
    tsqrt=[]
    tlog=[]
    for p in factorbase:
        ms=int(modular_sqrt(n,p))
        tsqrt.append(ms)
        tlog.append(log(p,10))
    xmax = len(factorbase)*60*4
    m_val = (xmax * root2n) >> 1
    thresh = log(m_val, 10) * 0.735
    #ignore small primes
    min_prime = int(thresh*3)
    fudge = sum(tlog[i] for i,p in enumerate(factorbase) if p < min_prime)/4
    thresh -= fudge
    
    roota=int(isqrt(root2n/xmax))
    roota=max(3,roota+int(roota&1==0))
    smooths=[]
    partials={}
    polynomials=0
    
    while 1:
        while 1:
            roota=next_prime(roota)
            if legendre_symbol(n,roota)==1:break
        polynomials+=1
        a = int(roota*roota)
        b = modular_sqrt(n,roota)
        b = int((b-(b*b-n)*mod_inv(2*b,roota))%a)
        c = int((b*b-n)/a)
        sievesize = 1<<15
        s1={};s2={}
        #set up values
        for i,p in enumerate(factorbase):
            ainv=pow(a,p-2,p)
            sol1=ainv*( tsqrt[i]-b) %p
            sol2=ainv*(-tsqrt[i]-b) %p
            sol1-=((xmax+sol1)/p)*p
            sol2-=((xmax+sol2)/p)*p
            s1[p]=int(sol1+xmax)
            s2[p]=int(sol2+xmax)
        #segmented sieve
        for low in xrange(-xmax,xmax+1,sievesize+1):
            high = min(xmax,low+sievesize)
            size=high - low
            S=[0.0]*(size+1)
            #sieve segment
            for i,p in enumerate(factorbase):
                if p<min_prime:continue
                sol1=s1[p]
                sol2=s2[p]
                logp=tlog[i]
                while sol1<=size or sol2<=size:
                    if sol1<=size:
                        S[sol1]+=logp
                        sol1+=p
                    if sol2<=size:
                        S[sol2]+=logp
                        sol2+=p
                s1[p]=int(sol1-size-1)
                s2[p]=int(sol2-size-1)
            #check segment for smooths
            for i in xrange(0,size+1):
                if S[i]>thresh:
                    x=i+low
                    tofact=nf=a*x*x+2*b*x+c
                    if nf<0:nf=-nf
                    for p in factorbase:
                    	while nf%p==0:nf=int(nf/p)
                    if nf==1:
                        smooths+=[(a*x+b,(tofact,roota))]
                    #check for 1 big factor
                    elif nf in partials:
                        pairv,pairvals=partials[nf]
                        smooths+=[( (a*x+b)*pairv, ( tofact*pairvals[0],roota*pairvals[1]*nf) )]
                        del partials[nf]
                    else:
                        partials[nf]=(a*x+b,(tofact,roota))
        if len(smooths)>len(factorbase):
            break
        if verbose:
            print 100*len(smooths)/len(factorbase),'%','using',polynomials,'polynomials','\r',
    if verbose:
        print len(smooths),"relations found using",polynomials,"polynomials"
    return algebra(factorbase,smooths,n)
 
n=input()
a=qs(n)
l=[a,n/a]
l.sort()
for i in l:
    print i,

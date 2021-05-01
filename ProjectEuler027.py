#Project Euler, Problem 27
#Quadratic primes

"""Euler discovered the remarkable quadratic formula:
    n**2 + n + 41
    It turns out that the formula will produce 40 primes for the consecutive integer values:
    0 <= n <= 39
    However, when n = 40, 40**2 + 40 + 41 = 40(40+1)+41 iis divisible by 41,
    and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.
    The incredible formula n**2 -79n +1601 was discovered, 
    which produces 80 primes for the consecutive values 0<=n<=79. 
    The product of the coefficients, −79 and 1601, is −126479.
    Considering quadratics of the form:
    n**2 +an + b, where mod(a) < 1000 and mod(b) <= 1000
    where mod(n) is the modulus of n
    eg. mod(11) = 11, mod(-4) = 4

    Find the product of the coefficients, a and b, for the quadratic expression 
    that produces the maximum number of primes for consecutive values of n,
    starting with n=0.
"""

import time

def isitprime(p):
    if p <= 0:
        return False
    for i in range(2,int(p**0.5)+1):
        if p % i == 0:
            return False
    return True

def possibleBprimes(Bmax):
    bprime = [1,2,3]
    for i in range(5,Bmax+1,2):
        if isitprime(i):
            bprime.append(i)
    return bprime

def possibleprimes(Amax,Bmax):
    blist = possibleBprimes(Bmax)
    alist = []
    for a in range(-(Amax-1),Amax):
        for b in blist:
            if b == 2:
                if a % 2:
                    if a + b + 1 > 0 and isitprime(a+b+1):
                        alist.append(a)
                else:
                    a -= 1
                    if a + b + 1 > 0 and isitprime(a+b+1):
                        alist.append(a)
            else:
                 if a + b + 1 > 0 and isitprime(a+b+1):
                        alist.append(a)
    return sorted(list(set(alist))), blist

def testequation(a,b):
    n = 0
    while True:
        test = n**2 + a*n + b
        if isitprime(test): n += 1
        else: break
    return n

def maxcoeff(Amax, Bmax):
    Alist, Blist = possibleprimes(Amax, Bmax)
    best = 0
    besta = 0
    bestb = 0
    for a in Alist:
        for b in Blist:
            c = testequation(a,b)
            if c > best: best, besta, bestb = c,a,b
    return besta*bestb

start = time.time()
print(maxcoeff(1000,1000))
print(time.time() - start)
#-59231 in 0.8406767845153809 secs
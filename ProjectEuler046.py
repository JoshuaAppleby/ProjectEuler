#Project Euler, Problem 46
#Goldbach's other conjecture

"""It was proposed by Christian Goldbach that every odd composite number can 
    be written as the sum of a prime and twice a square.
    9 = 7 + 2×1**2
    15 = 7 + 2×2**2
    21 = 3 + 2×3**2
    25 = 7 + 2×3**2
    27 = 19 + 2×2**2
    33 = 31 + 2×1**2
    It turns out that the conjecture was false.
    What is the smallest odd composite that cannot be written as 
    the sum of a prime and twice a square?
"""

import time

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3,int(n**0.5+1),2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3,n,2):
        if is_prime[i]:
            prime.append(i)
    return prime

def compute(x,c):
    for n in range(1,100):
        for j in x:
            conject = j + (2*(n**2))
            if conject ==c:
                return True
    return False

def goldbach():
    primes = sieve(10000)
    comp = []
    for k in range(1,10000,2):
        if k not in primes:
            comp.append(k)
    for c in comp:
        if c > 33:
            d = compute(primes,c)
            if d == False:
                return c

start = time.time()
print(goldbach())
print(time.time()-start)
#5777 in 2.0631790161132812 secs
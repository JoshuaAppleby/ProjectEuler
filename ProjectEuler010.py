#Project Euler, Problem 10
#Summation of primes

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

import time

def sieve(n):
    """Sieve of Eratosthenes up to a maximum range of n"""
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

def sumsieve(n):
    """Returns the sum of the list given
        Requires sieve(n)"""
    primelist = sieve(n)
    return sum(primelist)

start = time.time()
print(sumsieve(2000000))
print(time.time() - start)
#142913828922 in 0.723151683807373 secs
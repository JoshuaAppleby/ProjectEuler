#Project Euler, Problem 41
#Pandigital prime

"""We shall say that an n-digit number is pandigital if it makes 
    use of all the digits 1 to n exactly once. 
    For example, 2143 is a 4-digit pandigital and is also prime.
    What is the largest n-digit pandigital prime that exists?
"""

import time

def isitpandigital(N):
    for i in range(1,len(str(N))+1):
        if str(i) not in str(N):
            return False
    return True

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
    for i in range(1234567,n,2):
        if is_prime[i]:
            prime.append(i)
    return prime  

def pandigital(N):
    primes = sieve(N)[::-1]
    for i in primes:
        if isitpandigital(i):
            return i

start = time.time()
print(pandigital(7654321))
print(time.time() - start)
#7652413 in 3.2128167152404785 secs
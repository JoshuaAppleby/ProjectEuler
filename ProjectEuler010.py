#Project Euler, Problem 10
#Summation of primes

"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
"""
def isitprime(p):
    for i in range(2,int(p**0.5)+1):
        if p % i == 0:
            return False
    return True

def sumprime(N):
    total = 0
    prime = 1
    while prime < N:
        prime += 1
        if isitprime(prime):
            total += prime
    return total

print(sumprime(2000000))
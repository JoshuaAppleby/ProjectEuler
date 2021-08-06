#Project Euler, Problem 7
#10001st prime

#By listing the first six prime numbers: 
#2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10,001st prime number?

import time

def isitprime(p):
    """This function checks if the input p is a prime number and returns True or False"""
    for i in range(2,int(p**0.5)+1):
        if p % i == 0:
            return False
    return True

def numprime(n):
    """This function finds the n th prime number
        Requires isitprime(p)"""
    counter, prime, num = 0, 0, 2
    while counter != n:
        if isitprime(num):
            counter += 1
            prime = num
        num += 1
    return prime

start = time.time()
print(numprime(10001))
print(time.time() - start)
#104743 in 0.18550348281860352 secs
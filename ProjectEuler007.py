#Project Euler, Problem 7
#10001st prime

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?"""

def isitprime(p):
    for i in range(2,int(p**0.5)+1):
        if p % i == 0:
            return False
    return True

def numprime(n):
    counter = 0
    num = 2
    prime = 0
    while counter != n:
        if isitprime(num):
            counter += 1
            prime = num
        num += 1
    return prime

print(numprime(10001))
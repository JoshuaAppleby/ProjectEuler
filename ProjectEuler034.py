#Project Euler, Problem 34
#Digit factorials

"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

import time

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def isitfactorialsum(N):
    number = [int(x) for x in str(N)]
    total = 0
    for i in range(len(number)):
        total += factorial(number[i])
    if N == total:
        return True
    else:
        return False

def digitfactorials():
    total = 0
    for i in range(3,2540160):
        if isitfactorialsum(i):
            total += i
    return total

start = time.time()
print(digitfactorials())
print(time.time() - start)
#40730 in 10.83525013923645 secs
#Project Euler, Problem 47
#Distinct primes factors

"""The first two consecutive numbers to have two distinct prime factors are:
14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

import time

def consecprime():
    for i in range(210,1000000): 
        if checker(i) and checker(i+1):
            print(i)
            if checker(i+2) and checker(i+3):
                return i

def checker(n):                 
    primecheck = []
    loop = 2
    while loop <= n:
        if n % loop == 0:
            n //= loop
            primecheck.append(loop)
        else:
            loop+= 1
    if len(set(primecheck)) == 4:
        return True
    else:
        return False

start = time.time()
print(consecprime())
print(time.time() - start)
#134043 in 204.80708384513855 secs
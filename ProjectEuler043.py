#Project Euler, Problem 43
#Sub-string divisibility

"""The number, 1406357289, is a 0 to 9 pandigital number because it is 
    made up of each of the digits 0 to 9 in some order, but it also has a 
    rather interesting sub-string divisibility property.
    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. 
    In this way, we note the following:
    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17
    Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import time

def isitpandigital(N):
    for i in range(0,len(str(N))):
        if str(i) not in str(N):
            return False
    return True

def isitdivisable(N):
    num = str(N)
    primes = [2,3,5,7,11,13,17]
    for i in range(0,7):
        if int(num[i+1:i+4]) % primes[i] != 0:
            return False
    return True

def panlista():
    panlow = []
    for i in range(1406357289,1460357289+1,2):
        if isitdivisable(i):
            panlow.append(i)
    panhigh = []
    for i in range(4106357289,4160357289+1,2):
        if isitdivisable(i):
            panhigh.append(i)
    panprime = []
    for j in panlow:
        if isitpandigital(j):
            panprime.append(j)
    for j in panhigh:
        if isitpandigital(j):
            panprime.append(j)
    return sum(panprime)

start = time.time()
print(panlista())
print(time.time() - start)
#16695334890 in 49.1054368019104 secs
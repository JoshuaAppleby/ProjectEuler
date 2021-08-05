#Project Euler, Problem 49
#Prime Permutations

"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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

def fourdigitlist():
    fourdigit = []
    primelist = sieve(10000)
    for i in primelist:
        if i >= 1000:
            fourdigit.append(i)
    return fourdigit #1061 numbers

def isitperm(a, b):
    if a == b:
        return False
    stra = str(a)
    strb = str(b)
    digits1 = {digit: stra.count(digit) for digit in stra}
    digits2 = {digit: strb.count(digit) for digit in strb}
    return digits1 == digits2

def tripleprime():
    primelist = fourdigitlist()
    for i in primelist:
        for j in primelist:
            if i < j:
                k = j + (j-i)
                if k in primelist:
                    if (j-i) == (k-j) and i != 1487:
                        if isitperm(i,j) and isitperm(i,k):
                            final = str(i) + str(j) + str(k)
                            return final

start = time.time()
print(tripleprime())
print(time.time() - start)
#296962999629 in 2.2429416179656982 secs
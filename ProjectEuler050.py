#Project Euler, Problem 50
#Consecutive Prime Sum

"""The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
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

def consecprime():
    primelist = sieve(1000000)
    lengthsum = 0
    largestsum = 0
    lastvalue = len(primelist)

    for i in range(len(primelist)):
        for j in range(i+lengthsum, lastvalue):
            sol = sum(primelist[i:j])
            if sol < 1000000:
                if sol in primelist:
                    lengthsum = j-i
                    largestsum = sol
            else:
                lastvalue = j+1
                break
    return largestsum

start = time.time()
print(consecprime())
print(time.time() - start)
#997651 in 0.6186110973358154 secs
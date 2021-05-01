#Project Euler, Problem 23
#Non-abundant sums

"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import time

def sumdivisors(N):
    divisors = []
    for i in range(1, int((N/2)+1)):
        if N % i == 0:
            divisors.append(i)
    return sum(divisors)

def allabundantlist(A):
    abundlist = []
    for i in range(11,A):
        if sumdivisors(i) > i:
            abundlist.append(i)
    return abundlist

def nonabundsum(B):
    abundsum = set()
    abunlist = allabundantlist(B)
    totalnum = list(range(1,B+1))
    for j in range(len(abunlist)):
        for k in range(j, len(abunlist)):
            subtotal = abunlist[k] + abunlist[j]
            if subtotal <= B:
                abundsum.add(subtotal)
    return sum(totalnum) - sum(abundsum)

start = time.time()
print(nonabundsum(28123))
print(time.time() - start)
#4179871 in 14.187713861465454 secs
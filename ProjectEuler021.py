#Project Euler, Problem 21
#Amicable numbers

"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
    Evaluate the sum of all the amicable numbers under 10000.
"""

import time

def sumdivisors(N):
    divisors = []
    for i in range(1, N):
        if N % i == 0:
            divisors.append(i)
    return sum(divisors)

def sumamicable(maximum):
    total = 0
    for da in range(1, maximum):
        db = sumdivisors(da)
        if sumdivisors(db) == da and db != da:
            total += da
    return total

start = time.time()
print(sumamicable(10000))
print(time.time() - start)
#31626 in 4.6390345096588135 secs
#Project Euler, Problem 32
#Pandigital products

"""We shall say that an n-digit number is pandigital if it makes use 
of all the digits 1 to n exactly once; for example, the 5-digit number, 
15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be 
sure to only include it once in your sum.
"""

import time

p = set()

def is_pandigital(n, s=9):
    return len(n)==s and not '1234567890'[:s].strip(n)

def calc (n):
    for i in range(2,  99):
        j = i+1
        while i*j < 8999:
            if is_pandigital(str(i)+str(j)+str(i*j), n): p.add(i*j)
            j+= 1
    return sum(p)

start = time.time()
print(calc(9))
print(time.time() - start)
#45228 in 0.02789902687072754 secs
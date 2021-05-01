#Project Euler, Problem 24
#Lexicographic permutations
"""A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import time

numbers = ["0","1","2","3","4","5","6","7","8","9"]

def factoradicconvert(N):
    factorial = []
    quotient = N-1
    divisor = 1
    while quotient != 0:
        factorial.append(quotient % divisor)
        quotient = quotient // divisor
        divisor += 1
    flipped = factorial[::-1]
    final = ""
    for i in flipped:
        final += str(i)
    return final

def permutation(M):
    factoradic = factoradicconvert(M)
    outp = []
    count = 0
    while count < len(factoradic):
        num = int(factoradic[0])
        outp.append(numbers[num])
        numbers.pop(num)
        factoradic = factoradic[1:]
    ans = ""
    for i in outp:
        ans += str(i)
    return ans

start = time.time()
print(permutation(1000000))
print(time.time() - start)
#2783915460 in 0.0009982585906982422 secs
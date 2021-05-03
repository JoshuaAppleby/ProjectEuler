#Project Euler, Problem 36
#Double-base palindromes

"""The decimal number, 585 = 1001001001<2> (binary), is palindromic in both bases.
    Find the sum of all numbers, less than one million, 
    which are palindromic in base 10 and base 2.
    (Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import time

def binary(N):
    binarynum = []
    quotient = N
    while quotient != 0:
        binarynum.append(quotient%2)
        quotient = quotient // 2
    flipped = binarynum[::-1]
    final = ""
    for i in flipped:
        final += str(i)
    return final

def dualpalindrome(M):
    pal = []
    for i in range(1,M,2):
        if str(i) == str(i)[::-1]:
            bi = binary(i)
            if bi == str(bi)[::-1]:
                pal.append(i)
    return sum(pal)

start = time.time()
print(dualpalindrome(1000000))
print(time.time() - start)
#872187 in 0.2109677791595459 secs
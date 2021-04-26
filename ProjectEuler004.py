#Project Euler, Problem 4
#Largest palindrome product

"""A palindromic number reads the same both ways. 
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time

def largestpal(S, L):
    pal = []
    for i in range(S, L):
        for j in range(S, L):
            num = str(j*i)
            rev = num[::-1]
            if num == rev:
                pal.append(i*j)
    return max(pal)

start = time.time()
print(largestpal(100,999))
print(time.time() - start)
#906609 in 0.24933099746704102 secs

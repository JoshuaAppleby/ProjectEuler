#Project Euler, Problem 4
#Largest palindrome product

#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

import time

def largestpal(S, L):
    """This function will return the largest palindrome when given the the smallest S and largest L numbers allowed.
        In this case S is 100 since it is the smallest three digit number, and L is 999 as the largest three digit number"""
    pal = []
    for i in range(S, L):
        for j in range(S, L):
            num = str(j*i)
            if num == num[::-1]:
                pal.append(i*j)
    return max(pal)

start = time.time()
print(largestpal(100,999))
print(time.time() - start)
#906609 in 0.22977471351623535 secs
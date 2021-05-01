#Project Euler, Problem 30
#Digit fifth powers

"""Surprisingly there are only three numbers that can be written 
    as the sum of fourth powers of their digits:
    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44
    As 1 = 14 is not a sum it is not included.
    The sum of these numbers is 1634 + 8208 + 9474 = 19316.
    Find the sum of all the numbers that can be written as the sum 
    of fifth powers of their digits.
"""

import time

def isitsumpower(N):
    number = [int(x) for x in str(N)]
    total = 0
    for i in range(len(number)):
        total += number[i]**5
    return total

def fifthpower():
    total = 0
    for i in range(2,6*9**5):
        if i == isitsumpower(i):
            total += i
    return total

start = time.time()
print(fifthpower())
print(time.time() - start)
#443839 in 0.8469603061676025 secs
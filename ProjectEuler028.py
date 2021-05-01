#Project Euler, Problem 28
#Number spiral diagonals

"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
    21 22 23 24 25                      21       25
    20  7  8  9 10                         7   9
    19  6  1  2 11      diagonals only:      1 
    18  5  4  3 12                         5   3
    17 16 15 14 13                      17      13
    It can be verified that the sum of the numbers on the diagonals is 101.
    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import time

def spiraldiagonal(N):
    if N % 2 == 0:
        return "N not odd"
    else:
        sections = int((N-1)/2)
        total = 1
        for i in range(sections):
            num = N-(2*(i))
            total += (4*num*num - 6*(num-1))
    return total


start = time.time()
print(spiraldiagonal(1001))
print(time.time() - start)
#669171001 in 0.0009686946868896484 secs
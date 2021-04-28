#Project Euler, Problem 16
#Power digit sum

"""2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2**1000?
"""

import time


def twotothepower(N):
    number = 2**N
    sumnum = sum(int(digit) for digit in str(number))
    return sumnum

start = time.time()
print(twotothepower(1000))
print(time.time() - start)
#1366 in 0.0009984970092773438 secs
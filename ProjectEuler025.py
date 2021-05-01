#Project Euler, Problem 25
#1000-digit Fibonacci number

"""The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.
    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import time

def indexoffib(N):
    F1 = 1
    F2 = 1
    count = 0
    while len(str(F1)) < N or len(str(F2)) < N:
        F1 += F2
        F2 += F1
        count += 2
    
    if len(str(F1)) > N:
        count -= 1
        return count
    else:
        return count

start = time.time()
print(indexoffib(1000))
print(time.time() - start)
#4782 in 0.012996435165405273 secs
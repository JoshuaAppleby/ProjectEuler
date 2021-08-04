#Project Euler, Problem 48
#Self Powers

"""The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
    Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

import time

def selfpower(n):
    sum = 0
    for i in range(1,n+1):
        sum += (i**i)
    return sum

def last10digits():
    num = selfpower(1000)
    return str(num)[-10::]

start = time.time()
print(last10digits())
print(time.time() - start)
#9110846700 in 0.008076667785644531 secs
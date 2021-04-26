#Project Euler, Problem 15
#Lattice paths

"""Starting in the top left corner of a 2×2 grid,
    and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20×20 grid?
"""

import time

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def routes(N):
    return factorial(N*2)/(factorial(N)**2)

start = time.time()
print(routes(20))
print(time.time() - start)
#137846528820 in 0.0010080337524414062 secs
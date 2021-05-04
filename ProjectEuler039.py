#Project Euler, Problem 39
#Integer right triangles

"""If p is the perimeter of a right angle triangle with integral length sides, 
    {a,b,c}, there are exactly three solutions for p = 120.
    {20,48,52}, {24,45,51}, {30,40,50}
    For which value of p ≤ 1000, is the number of solutions maximised?
"""

import time

def get_abc(a, p):
    b = (p**2 - 2*p*a) / (2*p - 2*a)
    c = (a**2 + b**2)**0.5
    return (a, b, c)

def maxsol(N):
    d = dict()
    for p in range(12,N+1):
        d[p] = 0
        for a in range(1,p//3):
            (a, b, c) = get_abc(a, p)
            if c == int(c): 
                d[p] += 1
    return d

def keywithmaxval(N):
    d = maxsol(N)
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

start = time.time()
print(keywithmaxval(1000))
print(time.time() - start)
#840 in 0.1854715347290039 secs
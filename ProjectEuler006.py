#Project Euler, Problem 6
#Sum square difference

def sumdif(N):
    """The sum of the squares of the first ten natural numbers is,
        1**2 + 2**2 + ... + 10**2 = 385
        The square of the sum of the first ten natural numbers is,
        (1+2+...+10)**2 = 55**2 = 3025
        Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640
        Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    """
    sumofsquares = 0
    sumnat = 0
    for i in range(1,N+1):
        sumofsquares += i**2
    for i in range(1,N+1):
        sumnat += i
    sumsquare = sumnat**2
    return sumsquare - sumofsquares

print(sumdif(100))
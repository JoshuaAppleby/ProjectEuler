#Project Euler 1
#Multiples of 3 and 5

def sumof3or5(N):
    """"If we list all the natural numbers below 10 that are multiples of 3 or 5,
        we get 3, 5, 6 and 9. The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000.
    """
    total = 0
    for n in range(N):
        if n % 3 == 0 or n % 5 == 0:
            total += n   
    return total

print(sumof3or5(1000))
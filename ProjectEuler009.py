#Project Euler, Problem 9
#Special Pythagorean triplet

def spectriple(N):
    """ A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
        a**2 + b**2 = c**2
        For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
        There exists exactly one Pythagorean triplet for which a + b + c = 1000.
        Find the product abc.
    """
    for a in range(1,N-2):
        for b in range(a,N-2):
            c = N-a-b
            if a**2 + b**2 == c**2 and a+b+c==N:
                return a*b*c

print(spectriple(1000))
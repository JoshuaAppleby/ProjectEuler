#Project Euler, Problem 33
#Digit cancelling fractions

"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
    which is correct, is obtained by cancelling the 9s.
    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
    There are exactly four non-trivial examples of this type of fraction, 
    less than one in value, and containing two digits in the numerator and denominator.
    If the product of these four fractions is given in its lowest common terms, 
    find the value of the denominator.
"""

import time

def fractions(): 
    fraction = []
    for a in range(10, 100):
        for b in range(a + 1, 100):
            if b % 10 == 0: continue
            if str(a)[1] == str(b)[0]:
                if int(str(a)[0]) / int(str(b)[1]) == a / b:
                    fraction.append([a, b])
    result = [1, 1]
    for f in fraction:
        result[0] *= f[0]
        result[1] *= f[1]
    for i in range(2, result[0]):
        if i > result[0]: break
        while result[0] % i == 0 and result[1] % i == 0:
            result[0] /= i
            result[1] /= i
    return result[1]

start = time.time()
print(fractions())
print(time.time() - start)
#100 in 0.0019960403442382812 secs
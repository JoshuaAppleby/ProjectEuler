#Project Euler, Problem 17
#Number letter counts

"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
    The use of "and" when writing out numbers is in compliance with British usage.
"""

import time

def letters():
    onetonine = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
    tentonineteen = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
    tys = 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6
    twentytoninetynine = 10*(tys) + 8*(onetonine)
    ninetynine = onetonine + tentonineteen + twentytoninetynine
    hundred = 9*(7)
    hundrdand = 891*(10)
    hundreds = 100*(onetonine) + 9*(ninetynine) + hundred + hundrdand
    thousand = 11
    total = hundreds + thousand + ninetynine
    return total

start = time.time()
print(letters())
print(time.time() - start)
#21124 in 0.0009987354278564453 secs
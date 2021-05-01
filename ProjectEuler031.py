#Project Euler, Problem 31
#Coin sums

"""In the United Kingdom the currency is made up of pound (£) and pence (p). 
    There are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
    It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
"""

import time

def coincomb(N):
    count = 0
    for a in range(int((N/100) +1)):
        for b in range(int(1+(N-100*a)/50)):
            for c in range(int(1+(N-100*a-50*b)/20)):
                for d in range(int(1+(N-100*a-50*b-20*c)/10)):
                    for e in range(int(1+(N-100*a-50*b-20*c-10*d)/5)):
                        for f in range(int(1+(N-100*a-50*b-20*c-10*d-5*e)/2)):
                            count += 1
    count += 1 
    return count                       

start = time.time()
print(coincomb(200))
print(time.time() - start)
#73682 in 0.004954338073730469 secs
#Project Euler, Problem 40
#Champernowne's constant

"""An irrational decimal fraction is created by concatenating the positive integers:
    0.12345678910(1)112131415161718192021...
    It can be seen that the 12th digit of the fractional part is 1.
    If dn represents the nth digit of the fractional part, 
    find the value of the following expression.
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

import time

def decimallist(N):
    dec = str()
    for i in range(1,int(N/2)+1):
        dec += str(i)
    return dec

def value(N):
    num = decimallist(N)
    valuenum = int(num[0]) * int(num[9]) * int(num[99]) * int(num[999]) * int(num[9999]) * int(num[99999]) * int(num[999999])
    return valuenum

start = time.time()
print(value(1000000))
print(time.time() - start)
#210 in 0.2872002124786377 secs
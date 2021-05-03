#Project Euler, Problem 35
#Circular primes

"""The number, 197, is called a circular prime because all rotations of the 
    digits: 197, 971, and 719, are themselves prime.   
    There are thirteen such primes below 100: 
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    How many circular primes are there below one million?
"""

import time

def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3,int(n**0.5+1),2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3,n,2):
        if is_prime[i]:
            prime.append(i)
    return prime   

def circularprime(N):
    primes = sieve(N)
    count = 0
    for i in primes:
        flag = True
        number = i/10
        while number:
            if (number%10) % 2 == 0 or (number%10)%5 == 0:
                flag = False
                break
            number //= 10
        if flag:
            length = len(str(i))
            number = i
            count += 1
            for j in range(length):
                number = (number%10)*10**(length-1)+number//10
                if number not in primes:
                    count -= 1
                    break
    return count
            
start = time.time()
print(circularprime(1000000))
print(time.time() - start)
#55 in 2.7197794914245605 secs
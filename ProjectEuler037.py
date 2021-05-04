#Project Euler, Problem 37
#Truncatable primes

"""The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import time

def truncate(n):
	listi = []
	n = str(n)
	for i in range(0,len(n)):
		listi.append(int(n[i:]))
		listi.append(int(n[:i+1]))
	del listi[0]
	return listi

def check(n):
	if n == 1: return False
	if n == 2: return True
	for i in range(2,int(n/2)+1):
		if n%i == 0:
			return False
	return True

def is_list_prime(n):
	lista = truncate(n)
	for i in lista:
		if not check(i):
			return False
	return True

def main():
	truncs = []
	j = 11
	while len(truncs) < 11:
		if is_list_prime(j):
			truncs.append(j)
		j += 1
	return sum(truncs)

start = time.time()
print(main())
print(time.time() - start)
#748317 in 45.39645743370056 secs
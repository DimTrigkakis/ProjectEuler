# No optimization for truncated primes, which are concatenations of smaller primes
# Optimization for 2-3 skips on primes, as well as sqrt(number)

import time
import math

def truncatedLists(number):
	
	myList = []
	L = R = number	
	nL = len(str(L))-1

	for i in range(nL):
		L = L % 10**nL
		R = R / 10
		myList.append(L)
		myList.append(R)
		nL = len(str(L))-1

	myList.append(number)	
	myList.sort()
		
	return myList

def allPrimeList(number):
	z = truncatedLists(number)
	for x in z:
		if not isPrime(x):
			return False
	return True

def isPrime(number):
	if (number <= 1):
		return False
	elif (number <= 3):
		return True
	elif (number % 2 == 0 or number % 3 == 0):
		return False

	i = 5
	while i < 1+int(math.sqrt(number)):
		if number % i == 0:
			return False
		i += 2*(3 - i % 3)

	return True

# core
start = time.time()

L = []
mySum = 0
N = 7

while(len(L) < 11):
	N += 2*(3-N % 3)
	
	if (allPrimeList(N)):
		L.append(N)
		if (len(L) == 11):
			break
end = time.time()

print L,"Sum:",sum(L),"in time:",end-start

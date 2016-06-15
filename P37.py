import math

def truncatedLists(number):
	listL = []
	listR = []
	n = len(str(number))-1
	L = number
	R = number

	for i in range(n):
		nL = len(str(L))-1	
		L = L % (10**nL)
		R = R / (10)
		listL.append(L)
		listR.append(R)

	return ([number],listL,listR)

def primeList(number):
	(a,b,c) = truncatedLists(number)
	if not isPrime(number):
		return False
	for x in a+b+c:
		if not isPrime(x):
			return False
	return True

	
def isPrime(number):
	if (number == 0 or number == 1):
		return False
	for i in range(2, 1+int(math.sqrt(number))):
            if number % i == 0:
		return False
	return True

#############
# core

L = []
mySum = 0
N = 1000

while(len(L) < 11):
	print(L)
	N *= 2
	L = []	
	for i in range(8,N):
		if (primeList(i)):
			if (len(L) < 11):
				L.append(i)
mySum = sum(L)

# show our results
print(L,mySum)	

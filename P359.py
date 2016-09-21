import math

print "Hilbert's New Hotel"

floors = None

def perfect_square(n):
	if math.floor(math.sqrt(n)) == math.sqrt(n):
		return True
	return False

def assign_room(n):

	vacant = False
	try_floor = 0

	while True:
		
		floor_current = floors[try_floor]
	
		if len(floor_current) == 0:
			floor_current.append(n)
			break
		else:
			m = floor_current[-1]
			
			if perfect_square(n+m):
				floor_current.append(n)
				break
		
		if len(floors) <= try_floor+1:
			floors.append([])

		try_floor += 1
	
def print_hotel():
	print "CURRENT HOTEL"
	print floors

	print "Now printing floors"
	for f in floors:
		
		print f
		
def generate_assignments(n):
	for x in range(1,n+1):
		assign_room(x)

def P(f,r):	
	if len(floors) < f:
		return 0
	
	if len(floors[f-1]) < r:
		return 0

	return floors[f-1][r-1]

def print_product(f1,p1,f2,p2):
	return str(f1)+"^"+str(p1)+"*"+str(f2)+"^"+str(p2)+"\n\t\t"

def sum_P(pf1,pf2,pow1,pow2,f=P):
	sum = 0
	
	product = pf1**pow1*pf2**pow2
	
	for pf1_select in range(0,pow1+1):
		for pf2_select in range(0,pow2+1):
			
			f_final = pf1**pf1_select*pf2**pf2_select
			r_final = pf1**(pow1-pf1_select)*pf2**(pow2-pf2_select)
			p = f(f_final,r_final)
			sum += p
					
	return sum

def I(r):
	if  r % 2 == 1:
		return 1
	return -1

def triangle_sum(r):
	return (r-1)*(r)/2
		
def solve_P(f,r):
	
	if f % 2 == 0:
		x = f/2-1
		if f != 2:
			return solve_P(2,r+2*(x))-x*I(r)
		else:
			return triangle_sum(r+2*1)-1*I(r)
	elif f != 1:
		ff = f-1
		x = ff/2
		return solve_P(2,r+2*(x-1))+(2+(x-1))*I(r)	
	else:
		return triangle_sum(r+1)
floors = [[]]

generate_assignments(400) # Naive calculation method
print "FINAL SUM IS "+str(sum_P(2,3,1,1))
print_hotel() # This shows the pattern

print "FINAL SUM (solver) IS "+str(sum_P(2,3,27,12,solve_P)) # This is the fast solver

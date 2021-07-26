def pythTrip(a,b,c):
	return ((a**2)+(b**2)) == c**2

num = 1000
for c in range(1, num):
	for b in range(1, num):
		for a in range(1, num):
			if ((c+b+a ) == 1000) and (pythTrip(a,b,c) == True):
				print(f"a:{a} b:{b} c:{c}")
				break
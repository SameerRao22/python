import math

def factorize(num):
	factors= 0
	for x in range(1, int((math.sqrt(num))+1)):
		if int(num)%x == 0:		
			if num/x == x:
				factors += 1
			else:
				factors += 2
	return factors

def triangleNum(n): 
	number = 0
	for x in range(1,int(n)+1):
		number += x
	return number

factors = 0
x = 1
num = 0
while True:
	if factors >= 500:
		print(num)
		break
	num = triangleNum(x)
	factors = factorize(num)
	x += 1
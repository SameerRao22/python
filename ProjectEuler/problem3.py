'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
num  = long()
x = long()
max = long()
num = 600851475143
x = 2
while num != 1:
	if num % x != 0:
		x+= 1
	else:		
		num = num / x
		if x > max:
			max = x
print(max)
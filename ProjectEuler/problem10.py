import math
def sieve(n):
	y = 2
	nums = {x:True for x in range(2, n+1)}
	for i in range(2, (round(math.sqrt(n))+1)):
		y = 2
		if nums[i] == True:
			while i*y <= n:
				nums[i*y] = False
				y += 1
	primes = [x for x in nums if nums[x] == True]
	return primes

lst = []
lst = sieve(2000000)
sum = 0
for x in lst:
	sum += x
print(sum)
def prime(num):
	for x in range(2, num-1):
		if num % x == 0:
			return False
	return True

primes = []
num = 2
while len(primes) != 10001:
	if prime(num) == True:
		primes.append(num)
	num += 1
print(primes[-1])
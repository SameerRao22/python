def palindrome(num):
	if int(str(num)[::-1]) == num:
		return True
	return False

max = 0
for x in range(100, 1000):
	for y in range(100, 1000):
		num = x * y
		if palindrome(num) == True:
			if num > max:
				max = num
print(max)
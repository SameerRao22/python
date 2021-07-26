def factorial(number):
	answer1 = 1
	while number != 0:
		answer1 = number * answer1
		number = number -1
	return answer1
	
#answer = factorial(10)
#print(answer)
print(factorial(10))		
'''
Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 1 and 2, 
the first 10 terms will be:

			1, 2, 3, 5, 8, 13, 21, 34, 55, 98, ...

By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, find the sum of the 
even-valued terms.
'''

fib = [1, 2, 3]
sum = 0
x = 0
while (fib[-1] + fib[-2]) < 4000000:
	fib.append(fib[-1] + fib[-2])

for x in fib:
	if x % 2 == 0:
		sum += x
print(sum)
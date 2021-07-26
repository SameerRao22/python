i = 100
num =1
while i != 0:
	num *= i
	i -= 1
num = str(num)
sum = 0
for x in num:
	sum += int(x)
print(sum)
f = open('hundredNumbers.txt', 'r')
if f.mode == 'r':
	numbers = f.readlines()
sum = 0
for x in range(100):
	sum += int(numbers[x]) 
print(str(sum)[0:10])
sum = 0
square = 0
allSquares = [x**2 for x in range(1, 101)]
for x in allSquares:
	sum += x
for x in range(1, 101):
	square += x

square = square**2

print(sum - square)
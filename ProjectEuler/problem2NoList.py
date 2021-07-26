before = 1
next1 = 1
y = 0
print(before)
print(next1)
for x in range(1,100):
	print(next1+before)
	y = next1+before
	before = next1
	next1 = y
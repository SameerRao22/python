'''def horizontal(x,y,list1):
	sum = 0
	for i in range(4):
		sum += list1[x][y+i]
'''
fl = []
with open("grid.txt") as textFile:
    fl = [line for line in textFile]
'''for x in range(20):
	for y in range(59):
		print(f'{fl[x][y]}', end = '')
	print()
'''
print(fl)
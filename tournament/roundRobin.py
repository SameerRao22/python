from itertools import permutations

def listPrint(list1): 	
	for x in list1: 
		print(x)	

def roundR(teamList):
	size = len(teamList)
	matchups = list(permutations(teamList, 2))
	eMatchups = []
	listPrint(matchups)
	print()
	for x in reversed(range(size)):
		print(x)
import roundRobin as r
from itertools import permutations

print('enter the number of teams')
teamNum = input()
teamNum = int(teamNum)
print('there are',teamNum,'teams')

teams = []
for x in range(teamNum):
	teams.append(x+1)
#print(teams)
r.roundR(teams)
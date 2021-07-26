import roundRobin as r

print('enter the number of teams')
teamNum = int(input())

print('there are',teamNum,'teams')

teams = []
for x in range(teamNum):
	teams.append(x+1)
print(teams)
r.roundR()
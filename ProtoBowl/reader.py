import requests
import json
import os
import time



with open('data.json', 'r') as f:
    data1 = json.load(f)


tossups = data1['data']['tossups']

os.system('clear')

for x in tossups[0]['formatted_answer']:
	if x == " ":
		time.sleep(0.1) 
	print(x, end ="")
print()
print()
'''
#{tossups[0]['text']}
#len(tossups[0]['text'])
y = "bob#s"
print(len(y))
for x in range(len(y)):
	print(y[x])
	if y[x] in ["~!@#$%^&*(((()_+{|/.,><:'"]:
		y.pop(x)

print(y)
#system(f"say {y}")
#print(tossups[0]['answer'])
'''
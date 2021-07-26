import random
import os

os.system('clear')
print('im thinking of a number from 1 to 100')
x = input('p1 make a guess> ')
y = input('p2 make a guess> ')

number = random.randint(1, 100)

if (abs(number-x)) < (abs(number-y)):
	print('p1 wins')
elif (abs(number-x)) > (abs(number-y)):
	print('p2 wins')

print('the number was ' + str(number))
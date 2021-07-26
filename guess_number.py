import random

answer = random.randint(1, 100)
lives = 10

while True:
  guess = int(input("Guess a number> "))
  if lives == 1:
		 print('out of lives')
		 break
  if guess > answer:
     print('too big')
  elif guess < answer:
     print('too small')
  else:
      print('correct')
      break	
  lives = lives - 1
from turtle import *
from random import randint

def drawBoard():
  penup()
  goto(-140,140)
  for x in range(15):
    write(x+1, align='center')
    right(90)
    for x in range(8):
      penup()
      forward(10)
      pendown()
      forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)
  penup()


speed(0)
names = []
colors =['green', 'orange', 'blue', 'lavender']
flag = False
for x in range(4):
  names.append(Turtle())

drawBoard()

for num2 in range(4):
  names[num2].penup()
  names[num2].goto(-150,100+(num2*-30))
  names[num2].color(colors[num2])
  names[num2].shape('turtle')


while True:
  if flag == True:
    break
  for y in range(4):
    if names[y].xcor() >= 140:
      flag = True
      break
    names[y].forward(randint(0,10))
    

x = input()
from tkinter import *
import time
import tkinter
import tkinter.messagebox as tkmessagebox
import random
import sys
from tkinter import Tk

root = Tk()
root2 = Frame(root)
text = Text(root)


def check():
	num1 = int()
	num1 = number.get()
	text.insert(INSERT, str(num1) + '\n')
	if int(num1) > x:
		text.insert(INSERT, 'Your number is too big\n')
	elif int(num1) < x:
		text.insert(INSERT, 'Your number is too small\n')
	elif int(num1) == x:
		text.insert(INSERT, 'You have guessed the number good job\n')
		win = True
		time.sleep(1)
		root2.destroy()
	text.pack()




	
x = int()
x = random.randint(0,10)
win = bool

text.insert(INSERT, 'I am thinking of a number\n' )
text.insert(INSERT, 'What is it\n')
number = Entry(root2)
e1 = tkinter.Button(root2, text = "Enter", command = check)
text.pack()
number.pack()
e1.pack()
root2.pack()
root.mainloop()
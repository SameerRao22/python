from tkinter import Tk
from tkinter import *
import time
import tkinter
import tkinter.messagebox as tkmessagebox


root = Tk()
text = Text(root)
def hello1():
	text.insert(INSERT, number.get() + '\n')
	text.pack()

root.title = ('Hello')
root.geometry('200x200')
def hello():
   text.insert(INSERT, number.get())
   text.pack()

number = Entry(root)
number.pack()
bob = tkinter.Button(root, text ='enter', command = hello)
bill = tkinter.Button(root, text ='bye', command = hello1)
bob.pack(expand=1)
bill.pack()
hello1()
root.mainloop()
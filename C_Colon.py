import os 
import shutil

y = input('directory or file ')
if y == 'directory': 
	x = input('enter something to delete ')
	shutil.rmtree(x)
elif y == 'file':
	x = input('enter something to delete ')
	os.remove(x)
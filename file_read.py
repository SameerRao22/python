import os

f= open("bob1.txt","w+")
f.write("This is bob\n")
f.write("I am awesome")
f.close

f = open("bob1.txt", "r+")
val = f.read()
print(val)
input()

#os.remove("C:/Users/krishnamurthys/Desktop/python/bob.txt")


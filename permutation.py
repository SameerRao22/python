def factorial(size):
	ans = 1
	for x in range(1, size+1):
		ans = x*ans
	return(ans)

print("enter a string")
string1 = input()
size = len(string1)
num = factorial(size)
print(string1[0], end="")
print("hi")
for x in range(num):
	
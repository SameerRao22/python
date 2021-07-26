TODO_LIST = ['DO HOMEWORK', 'WATCH TV', 'SLEEP']

def done():
	print('ARE YOU done WITH ', TODO_LIST[0])
	yes_or_no = input()
	if yes_or_no == 'yes':
		print('OK REMOVING IT')
		REMOVED = TODO_LIST.pop(0)
		print('REMOVED ', REMOVED)
	elif yes_or_no == 'no':
		print('DO IT!!!')
		done()		
	else:
		print('INVALID CHAR ENTERED TRY AGAIN')
		done()

def add(list1):
	print('ok')
	item = input('what would you like to add ')
	index = input('what position would you like it to be in ')
	index = int()
	list1.insert(index, item)
	#list1[index] = item
	return list1

		
print('this is your to-do list')
print(TODO_LIST)

print('would you like to add something to the list')
choice = input()
if choice == 'yes':
	TODO_LIST = add(TODO_LIST)
	print(TODO_LIST)
	
elif choice == 'no':
	print('ok on to completing your list');
while len(TODO_LIST) != 0:
	done()

print('YOU ARE GOOD TO GO')


	
	
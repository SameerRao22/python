from socket import *
import os


host = '192.168.1.80'
port = 10001
s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print 'Type in <EXIT> to leave the chat room'
'''
print(s.recv(1024)) 
s.close()
-----------------------------
s.connect((host, port))
os.system('clear')
print(s.recv(1024)) 

while True:
	data = s.recv(1024)
	print(repr(data))
	if not data: break
	reply = raw_input('Reply: ')
	s.sendall(reply)

s.close()
'''
while True:
	message = raw_input('Your Message: ')
	if message == '<EXIT>': break
	s.send(message)
	reply = s.recv(1024)
	print 'got ',repr(reply) 

s.close()

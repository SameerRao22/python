from socket import *


s = socket(AF_INET, SOCK_STREAM)
#host = socket.gethostname()
host = '192.168.1.80'
port = 10001
s.bind((host, port))

s.listen(1)
c, addr = s.accept()
print addr, ' connected'
print 'Type in <EXIT> to leave the chat room'
while True:
	data = c.recv(1024)
	print 'got ', repr(data) 
	reply = raw_input('Reply: ')
	if reply == '<EXIT>': break
	c.sendall(reply)

c.close()



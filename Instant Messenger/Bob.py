import socket
import time
import math

#p=11
#q=31
#phi=300
n = 341
e = 7
d = 43

def encrypt(dat):
	ct = ''
	for m in dat:
		m = ord(m)
		"print 'ord',m"
		z = int((math.pow(m,e)) % n)
		if z<99:
			ct = ct+'0'
		i = ''.join(str(int(z)))
		"print i"
		ct = ct + i
	return (ct)

def decrypt(dat,leng):
	pt = ''
	a=0
	b=a+3
	for i in range (0,leng):
		c = int(dat[a:b])
		m = ((c**d) % n)
		m = chr(m)
		pt = pt + m
		a = a+3
		b = a+3
	return pt

host = socket.gethostbyname('localhost')
port = 3101
client = ('127.0.0.1', 1101)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host,port))
	
message = raw_input("Me: ")
cipher = encrypt(message)
print "Data sent:",cipher
while message != 'q':
	sock.sendto(cipher, client)
	time.sleep(5)
	data, addr = sock.recvfrom(1024)
	l = (len(data))/3
	plain = decrypt(data,l)
	print "Decrypted message:",plain
	print "Client: " + str(data)
	message = raw_input("Me: ")
	cipher = encrypt(message)
	print "Data sent:",cipher
sock.close()



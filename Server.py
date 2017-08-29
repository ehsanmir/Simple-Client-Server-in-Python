import socket
import struct
import time

while True:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind(('192.168.213.1', 4444))
	sock.listen(1)
	print ('Waiting for a Connection...')
	(client, (ip,sock)) = sock.accept()
	counter = 1
	while True:
		try:
			data = client.recv(1024)
			if not data:
				break
			print ("Recieving Packet Number %d" %counter)
			print(data)
			counter += 1
		except:
			break
	print("Connection Closed!")
	client.close()
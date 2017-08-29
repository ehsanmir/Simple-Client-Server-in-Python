import socket
import struct
import random
from random import randint
import string
import time

s = socket.socket()
host = '192.168.213.1'
port = 4444
s.connect((host, port))

commands = ["user", "pass", "abc", "def", "ghi", "jkl", "mno", "exit"]
delimiter = "/"
counter = 1
while True:
	field1 = commands[randint(0, 7)]
	field2 = str(randint(0, 999))
	field3 = ''.join(random.choice(string.ascii_lowercase) for i in range(randint(5, 50)))
	field4 = '123'
	field5 = ''.join(random.choice(string.ascii_lowercase) for i in range(randint(5, 50)))
	buffer = field1 + delimiter + field2 + delimiter + field3 + field4 + field5
	print ("Sending Packet Number %d" %counter)
	print (buffer)
	s.send(buffer.encode())
	time.sleep(2)
	counter += 1
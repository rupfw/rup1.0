from socket import *
import sys
import os.path
import json

blksz = 1024

if len(sys.argv) < 2:
	print 'Server Port No. missing in command line arguments'
	serverControlPort = raw_input('Enter Server Port No.: ')
else:
	serverControlPort = sys.argv[1]

serverIP = '127.0.0.1'
clientControlSocket = socket(AF_INET, SOCK_STREAM) 

#Function Start here--
def ReceiveFile(filename):
	try:
		filepath = "Client/"+filename
		file = open(filepath, 'wb') # create local file in cwd
		while True:
			data = clientControlSocket.recv(blksz) # get up to 1K at a time
			if not data: break # till closed on server side
			file.write(data) # store data in local file
		print 'File Received.'
		file.close()
		return 0
	except:
		file.close()
		return -1
#Function end here--

try:
	clientControlSocket.connect((serverIP,int (serverControlPort)))
	file = "\Server\PLT.pdf"; 
	clientControlSocket.send(file)
	ReceiveFile(file)
	ControlConRecv = clientControlSocket.recv(1024) 

	print (ControlConRecv)

	clientControlSocket.close()
except:
	clientControlSocket.close()


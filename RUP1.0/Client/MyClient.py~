from socket import *
import sys
import os.path
import json

blksz = 1024

if len(sys.argv) < 2:
	print 'Server Port No. missing in command line arguments'
	serverPort = raw_input('Enter Server Port No.: ')
else:
	serverPort = sys.argv[1]

serverIP = '127.0.0.1'
clientSocket = socket(AF_INET, SOCK_STREAM) 

#Function Start here--
def ReceiveFile(filename):
	try:
		filepath = filename
		file = open('testfile', 'wb') # create local file in cwd
		while True:
			data = clientSocket.recv(blksz) # get up to 1K at a time
			if not data: break # till closed on server side
			file.write(data) # store data in local file
		file.close()
		print 'File Received.'
		return 0
	except:
		print 'File Receiving Error'
		file.close()
		return -1
#Function end here--

try:
	clientSocket.connect((serverIP,int (serverPort)))
	file = "PLT.pdf"; 
	clientSocket.send(file)
	ReceiveFile(file)
	ControlConRecv = clientSocket.recv(1024) 
	print (ControlConRecv)
	clientSocket.close()
except:
	clientSocket.close()

